#requires -Version 7.0

[CmdletBinding()]
param(
    [ValidateSet('Prepare', 'Simulate', 'Run', 'Resume', 'Reconcile', 'Cancel', 'SelfTest')]
    [string]$Mode = 'Prepare',

    [string]$PackagePath,
    [string]$Workdir,
    [string]$CampaignId = 'SRD-607',
    [string]$SupervisorRoot = $PSScriptRoot,
    [string]$Model = 'gpt-5.6-luna',
    [ValidateSet('minimal', 'low', 'medium', 'high', 'xhigh', 'max', 'ultra')]
    [string]$ReasoningEffort = 'max',
    [ValidateSet('normal', 'early-complete', 'failure')]
    [string]$SimulationScenario = 'normal',
    [ValidateRange(1, 1000)]
    [int]$SimulationCycles = 2,
    [int]$ExpectedLastLot = 20,
    [int]$RequiredBaseLot = 20,
    [switch]$RetryFailed
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$script:SupervisorRoot = [IO.Path]::GetFullPath($SupervisorRoot)
$script:StateDir = Join-Path $script:SupervisorRoot 'state'
$script:RunsDir = Join-Path $script:SupervisorRoot 'runs'
$script:LogsDir = Join-Path $script:SupervisorRoot 'logs'
$script:StatePath = Join-Path $script:StateDir 'campaign.json'
$script:HistoryPath = Join-Path $script:StateDir 'history.jsonl'
$script:LockPath = Join-Path $script:StateDir 'campaign.lock'
$script:BundledPythonPath = Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'

function Ensure-Directory {
    param([Parameter(Mandatory)][string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) {
        New-Item -ItemType Directory -Path $Path -Force | Out-Null
    }
}

foreach ($directory in @($script:SupervisorRoot, $script:StateDir, $script:RunsDir, $script:LogsDir)) {
    Ensure-Directory -Path $directory
}

function Get-UtcTimestamp {
    return (Get-Date).ToUniversalTime().ToString('o')
}

function ConvertTo-JsonText {
    param([Parameter(Mandatory)]$Value)
    return ($Value | ConvertTo-Json -Depth 30 -Compress)
}

function Write-AtomicText {
    param(
        [Parameter(Mandatory)][string]$Path,
        [Parameter(Mandatory)][AllowEmptyString()][string]$Text
    )
    Ensure-Directory -Path (Split-Path -Parent $Path)
    $temporary = "$Path.$([guid]::NewGuid().ToString('N')).tmp"
    try {
        [IO.File]::WriteAllText($temporary, $Text, [Text.UTF8Encoding]::new($false))
        Move-Item -LiteralPath $temporary -Destination $Path -Force
    }
    finally {
        if (Test-Path -LiteralPath $temporary) {
            Remove-Item -LiteralPath $temporary -Force -ErrorAction SilentlyContinue
        }
    }
}

function Write-AtomicJson {
    param(
        [Parameter(Mandatory)][string]$Path,
        [Parameter(Mandatory)]$Value
    )
    Write-AtomicText -Path $Path -Text (ConvertTo-JsonText -Value $Value)
}

function Redact-Secrets {
    param([AllowNull()][string]$Text)
    if ($null -eq $Text) { return '' }
    $result = $Text
    $result = [regex]::Replace($result, '(?i)(bearer\s+|api[_-]?key\s*[:=]\s*|secret\s*[:=]\s*|password\s*[:=]\s*)[^\s\r\n,;]+', '$1[REDACTED]')
    $result = [regex]::Replace($result, '(?i)(sk-[A-Za-z0-9_-]{12,}|gh[pousr]_[A-Za-z0-9_]{12,}|xox[baprs]-[A-Za-z0-9-]{12,})', '[REDACTED]')
    return $result
}

function Add-HistoryEvent {
    param(
        [Parameter(Mandatory)][string]$Event,
        [Parameter(Mandatory)]$Data
    )
    $record = [ordered]@{
        at = Get-UtcTimestamp
        event = $Event
        data = $Data
    }
    Add-Content -LiteralPath $script:HistoryPath -Value (Redact-Secrets (ConvertTo-JsonText -Value $record)) -Encoding utf8NoBOM
}

function New-CampaignState {
    return [ordered]@{
        schema_version = 1
        campaign_id = $CampaignId
        status = 'PENDING'
        created_at = Get-UtcTimestamp
        updated_at = Get-UtcTimestamp
        codex = [ordered]@{
            model = $Model
            reasoning_effort = $ReasoningEffort
            version = $null
            required_options = @('-C', '-s', '--json', '-o')
        }
        package_base = [ordered]@{
            path = $null
            sha256 = $null
            last_lot = $null
            required_base_lot = $null
        }
        target = [ordered]@{
            total = $null
            complete_fichas = $null
            verified_images = $null
        }
        workdir = $null
        counts = [ordered]@{
            complete_fichas = $null
            verified_images = $null
            ids = $null
        }
        next_cycle = $null
        current_cycle = $null
        attempts = @()
        dispatches = @()
        last_error = $null
    }
}

function Read-CampaignState {
    if (-not (Test-Path -LiteralPath $script:StatePath)) { return $null }
    return (Get-Content -Raw -LiteralPath $script:StatePath | ConvertFrom-Json)
}

function Save-CampaignState {
    param([Parameter(Mandatory)]$State)
    $State.updated_at = Get-UtcTimestamp
    Write-AtomicJson -Path $script:StatePath -Value $State
}

function Set-ObjectProperty {
    param(
        [Parameter(Mandatory)]$Object,
        [Parameter(Mandatory)][string]$Name,
        [AllowNull()]$Value
    )
    $property = $Object.PSObject.Properties[$Name]
    if ($null -eq $property) {
        $Object | Add-Member -MemberType NoteProperty -Name $Name -Value $Value -Force
    }
    else {
        $property.Value = $Value
    }
}

function New-LockHandle {
    Ensure-Directory -Path $script:StateDir
    for ($attempt = 0; $attempt -lt 2; $attempt++) {
        try {
            $stream = [IO.File]::Open($script:LockPath, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::None)
            $lockInfo = [ordered]@{
                campaign_id = $CampaignId
                process_id = $PID
                acquired_at = Get-UtcTimestamp
            }
            $bytes = [Text.UTF8Encoding]::new($false).GetBytes((ConvertTo-JsonText -Value $lockInfo))
            $stream.Write($bytes, 0, $bytes.Length)
            $stream.Flush()
            return $stream
        }
        catch [IO.IOException] {
            if ($attempt -eq 0 -and (Test-Path -LiteralPath $script:LockPath)) {
                $staleOwnerPid = $null
                try {
                    $lockInfo = Get-Content -Raw -LiteralPath $script:LockPath | ConvertFrom-Json
                    if ($lockInfo.process_id) { $staleOwnerPid = [int]$lockInfo.process_id }
                }
                catch { $staleOwnerPid = $null }
                $ownerAlive = if ($staleOwnerPid) { $null -ne (Get-Process -Id $staleOwnerPid -ErrorAction SilentlyContinue) } else { $true }
                if ($staleOwnerPid -and -not $ownerAlive) {
                    Remove-Item -LiteralPath $script:LockPath -Force -ErrorAction SilentlyContinue
                    continue
                }
            }
            throw [InvalidOperationException]::new('CAMPAIGN_LOCK_HELD: outra execução já mantém o lock desta campanha.')
        }
    }
    throw [InvalidOperationException]::new('CAMPAIGN_LOCK_HELD: não foi possível adquirir o lock da campanha.')
}

function Release-LockHandle {
    param([AllowNull()][IO.FileStream]$Handle)
    if ($null -eq $Handle) { return }
    $Handle.Dispose()
    if (Test-Path -LiteralPath $script:LockPath) {
        Remove-Item -LiteralPath $script:LockPath -Force -ErrorAction SilentlyContinue
    }
}

function Get-Sha256 {
    param([Parameter(Mandatory)][string]$Path)
    return (Get-FileHash -Algorithm SHA256 -LiteralPath $Path).Hash.ToLowerInvariant()
}

function Get-ObjectValue {
    param(
        [Parameter(Mandatory)]$Object,
        [Parameter(Mandatory)][string[]]$Names
    )
    foreach ($name in $Names) {
        $property = $Object.PSObject.Properties[$name]
        if ($null -ne $property) { return [string]$property.Value }
    }
    return ''
}

function Get-ZipText {
    param(
        [Parameter(Mandatory)][IO.Compression.ZipArchive]$Zip,
        [Parameter(Mandatory)][string]$Name
    )
    $entry = $Zip.GetEntry($Name)
    if ($null -eq $entry) { throw "ZIP_ENTRY_MISSING:$Name" }
    $reader = [IO.StreamReader]::new($entry.Open(), [Text.UTF8Encoding]::new($false, $true))
    try { return $reader.ReadToEnd() }
    finally { $reader.Dispose() }
}

function Get-ZipEntryHash {
    param([Parameter(Mandatory)][IO.Compression.ZipArchiveEntry]$Entry)
    $sha = [Security.Cryptography.SHA256]::Create()
    $stream = $Entry.Open()
    try { return ([BitConverter]::ToString($sha.ComputeHash($stream)).Replace('-', '')).ToLowerInvariant() }
    finally {
        $stream.Dispose()
        $sha.Dispose()
    }
}

function Test-ZipReadable {
    param([Parameter(Mandatory)][IO.Compression.ZipArchive]$Zip)
    foreach ($entry in $Zip.Entries) {
        if ($entry.FullName.EndsWith('/')) { continue }
        $source = $entry.Open()
        $sink = [IO.MemoryStream]::new()
        try { $source.CopyTo($sink) }
        finally {
            $source.Dispose()
            $sink.Dispose()
        }
    }
    return $true
}

function Test-DocxEntry {
    param(
        [Parameter(Mandatory)][IO.Compression.ZipArchive]$OuterZip,
        [Parameter(Mandatory)][string]$Name
    )
    $entry = $OuterZip.GetEntry($Name)
    if ($null -eq $entry) { return $false }
    $source = $entry.Open()
    $memory = [IO.MemoryStream]::new()
    try {
        $source.CopyTo($memory)
        $memory.Position = 0
        $docx = [IO.Compression.ZipArchive]::new($memory, [IO.Compression.ZipArchiveMode]::Read, $true)
        try { return ($null -ne $docx.GetEntry('word/document.xml')) }
        finally { $docx.Dispose() }
    }
    finally {
        $source.Dispose()
        $memory.Dispose()
    }
}

function Test-NestedZipEntry {
    param(
        [Parameter(Mandatory)][IO.Compression.ZipArchive]$OuterZip,
        [Parameter(Mandatory)][string]$Name
    )
    $entry = $OuterZip.GetEntry($Name)
    if ($null -eq $entry) { return $false }
    $source = $entry.Open()
    $memory = [IO.MemoryStream]::new()
    try {
        $source.CopyTo($memory)
        $memory.Position = 0
        $nested = [IO.Compression.ZipArchive]::new($memory, [IO.Compression.ZipArchiveMode]::Read, $true)
        try { Test-ZipReadable -Zip $nested | Out-Null; return $true }
        finally { $nested.Dispose() }
    }
    finally {
        $source.Dispose()
        $memory.Dispose()
    }
}

function Get-CsvRowsFromText {
    param([Parameter(Mandatory)][string]$Text)
    $rows = @($Text | ConvertFrom-Csv -Delimiter ';')
    return $rows
}

function Get-DuplicateValues {
    param([Parameter(Mandatory)][string[]]$Values)
    return @($Values | Where-Object { $_ } | Group-Object | Where-Object Count -gt 1 | ForEach-Object Name)
}

function Test-ReportCount {
    param(
        [Parameter(Mandatory)][string]$Report,
        [Parameter(Mandatory)][int]$Count,
        [Parameter(Mandatory)][string]$Pattern
    )
    foreach ($line in ($Report -split '\r?\n')) {
        if ($line -match $Pattern -and $line -match "(?<!\d)$Count(?!\d)") { return $true }
    }
    return $false
}

function Test-ContinuityPackage {
    [OutputType([pscustomobject])]
    param(
        [Parameter(Mandatory)][string]$Path,
        [int]$ExpectedLastLot = 20,
        [int]$RequiredBaseLot = 20
    )

    $errors = [Collections.Generic.List[object]]::new()
    $result = [ordered]@{
        pass = $false
        code = 'UNVALIDATED'
        detail = ''
        path = $Path
        sha256 = $null
        expected_last_lot = $ExpectedLastLot
        required_base_lot = $RequiredBaseLot
        base_candidates = @()
        base_package = $null
        last_lot = $null
        next_cycle = $null
        counts = [ordered]@{ ids = $null; complete_fichas = $null; verified_images = $null }
        manifest = [ordered]@{ entries = 0; checked = 0; mismatches = @() }
        required_files = @()
        errors = @()
    }

    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        $result.code = 'PACKAGE_NOT_FOUND'
        $result.detail = 'O pacote de continuidade não existe no caminho informado.'
        $result.errors = @($result.detail)
        return [pscustomobject]$result
    }
    $result.sha256 = Get-Sha256 -Path $Path

    $zip = $null
    try {
        $zip = [IO.Compression.ZipFile]::OpenRead($Path)
        Test-ZipReadable -Zip $zip | Out-Null
    }
    catch {
        $result.code = 'ZIP_INVALID'
        $result.detail = "O ZIP não pôde ser aberto/lido: $($_.Exception.Message)"
        $result.errors = @($result.detail)
        if ($null -ne $zip) { $zip.Dispose() }
        return [pscustomobject]$result
    }

    try {
        $names = @($zip.Entries | ForEach-Object FullName)
        $unsafe = @($names | Where-Object { $_ -match '(^|/)\.\.(/|$)' -or $_ -match '^/' })
        if ($unsafe.Count -gt 0) { $errors.Add('ZIP_PATH_TRAVERSAL_OR_ABSOLUTE_ENTRY') }
        if ((@($names | Sort-Object -Unique)).Count -ne $names.Count) { $errors.Add('ZIP_DUPLICATE_ENTRY') }

        $artifactJson = @($names | Where-Object { $_ -match '^02_SAIDA_[^/]+/SRD_FICHAS_607\.json$' })
        $artifactRoots = @($artifactJson | ForEach-Object { ($_ -split '/')[0] } | Sort-Object -Unique)
        if ($artifactRoots.Count -ne 1) { $errors.Add('ARTIFACT_ROOT_AMBIGUOUS_OR_MISSING') }
        $artifactRoot = if ($artifactRoots.Count -eq 1) { $artifactRoots[0] } else { '02_SAIDA_V2.0.0' }
        $artifactSource = @($names | Where-Object { $_ -match ("^$([regex]::Escape($artifactRoot))/SRD_Card_Game_Fichas_607_Fontes_Web_.+\.csv$") })
        if ($artifactSource.Count -ne 1) { $errors.Add('SOURCE_INDEX_AMBIGUOUS_OR_MISSING') }
        $artifactZip = @($names | Where-Object { $_ -match ("^$([regex]::Escape($artifactRoot))/SRD_FICHAS_IMAGENS_607_.+\.zip$") })
        if ($artifactZip.Count -ne 1) { $errors.Add('OUTPUT_ZIP_AMBIGUOUS_OR_MISSING') }
        $jsonName = "$artifactRoot/SRD_FICHAS_607.json"
        $auditName = "$artifactRoot/SRD_AUDITORIA_PENDENCIAS_607.csv"
        $imageCsvName = "$artifactRoot/SRD_URLS_IMAGENS_607.csv"
        $fichasDocxName = "$artifactRoot/SRD_FICHAS_607_COMPLETAS.docx"
        $imagesDocxName = "$artifactRoot/SRD_URLS_IMAGENS_607.docx"
        $reportName = "$artifactRoot/SRD_RELATORIO_DE_COLETA.md"
        $nestedZipName = if ($artifactZip.Count -eq 1) { $artifactZip[0] } else { "$artifactRoot/SRD_FICHAS_IMAGENS_607_v2.0.0_2026-10-10.zip" }
        $required = @(
            '01_CONTINUIDADE/ESTADO_ATUAL.md',
            '01_CONTINUIDADE/MANIFESTO_SHA256.json',
            '01_CONTINUIDADE/PROMPT_PROXIMO_PROCESSO.txt',
            $jsonName,
            $auditName,
            $(if ($artifactSource.Count -eq 1) { $artifactSource[0] } else { "$artifactRoot/SRD_Card_Game_Fichas_607_Fontes_Web_Lote.csv" }),
            $imageCsvName,
            $fichasDocxName,
            $imagesDocxName,
            $reportName,
            $nestedZipName,
            '03_CONSTRUTOR/LEIA-ME.txt',
            '03_CONSTRUTOR/build_deliverables.py',
            '03_CONSTRUTOR/SRD_Card_Game_Fichas_607_Indice_e_Textos_Extraidos.json',
            '03_CONSTRUTOR/SRD_Worker_Base_Pendencias_607.csv',
            '04_INSUMOS/SRD_Worker_Prompt_Completo_Fichas_Imagens_607.txt',
            '04_INSUMOS/SRD_Worker_Manifesto_607.json'
        )
        $result.required_files = $required
        $missing = @($required | Where-Object { $null -eq $zip.GetEntry($_) })
        if ($missing.Count -gt 0) { $errors.Add("REQUIRED_FILES_MISSING:$($missing -join ',')") }

        $baseCandidates = @($names | Where-Object { $_ -match '^00_PACOTE_BASE/[^/]+\.zip$' })
        $result.base_candidates = $baseCandidates
        $baseMatch = @($baseCandidates | Where-Object { $_ -match ("(?i)LOTE$RequiredBaseLot(?:[^0-9]|$)") })
        if ($RequiredBaseLot -eq 0 -and $baseCandidates.Count -eq 0) {
            $result.base_package = $null
        }
        elseif ($baseMatch.Count -ne 1) {
            if ($RequiredBaseLot -gt 0 -and $baseCandidates.Count -gt 0) {
                $errors.Add("BASE_PACKAGE_LOTE$RequiredBaseLot_REQUIRED:encontrado(s) $($baseCandidates -join ',')")
            }
            elseif ($RequiredBaseLot -gt 0 -and $baseCandidates.Count -eq 0) {
                $errors.Add("BASE_PACKAGE_MISSING:LOTE$RequiredBaseLot")
            }
            else {
                $errors.Add("BASE_PACKAGE_AMBIGUOUS:esperado LOTE$RequiredBaseLot; encontrado(s) $($baseCandidates -join ',')")
            }
        }
        else { $result.base_package = $baseMatch[0] }

        $stateText = Get-ZipText -Zip $zip -Name '01_CONTINUIDADE/ESTADO_ATUAL.md'
        $lotPattern = "(?i)\bLOTE\s*$ExpectedLastLot\b"
        if ($stateText -notmatch $lotPattern) { $errors.Add("CHECKPOINT_LAST_LOT_MISMATCH:esperado LOTE$ExpectedLastLot") }
        if ($stateText -notmatch '(?i)28.*homebrew|homebrew.*28' -or $stateText -notmatch '(?i)(exclu|reintrodu)') {
            $errors.Add('OWN_HOMEBREW_EXCLUSION_UNPROVEN')
        }

        $promptText = Get-ZipText -Zip $zip -Name '01_CONTINUIDADE/PROMPT_PROXIMO_PROCESSO.txt'
        $rangeMatch = [regex]::Match($promptText, '(?i)lotes?\s*(?:de\s*)?(\d+)\s*(?:a|[-–])\s*(\d+)')
        if (-not $rangeMatch.Success) {
            $listMatch = [regex]::Match($promptText, '(?im)^\s*Trabalhe exatamente nos lotes\s+([^\r\n]+)')
            if ($listMatch.Success) {
                $listedLots = @([regex]::Matches($listMatch.Groups[1].Value, '\d+') | ForEach-Object { [int]$_.Value })
                if ($listedLots.Count -ge 5) {
                    $firstFiveLots = @($listedLots | Select-Object -First 5)
                    $consecutive = $true
                    for ($lotIndex = 1; $lotIndex -lt $firstFiveLots.Count; $lotIndex++) {
                        if ($firstFiveLots[$lotIndex] -ne $firstFiveLots[$lotIndex - 1] + 1) { $consecutive = $false }
                    }
                    if ($consecutive) {
                        $rangeMatch = [regex]::Match("lotes $($firstFiveLots[0]) a $($firstFiveLots[4])", '(?i)lotes?\s*(\d+)\s*(?:a|[-–])\s*(\d+)')
                    }
                }
            }
        }
        if (-not $rangeMatch.Success) {
            $errors.Add('NEXT_CYCLE_RANGE_NOT_DECLARED')
        }
        else {
            $result.next_cycle = [ordered]@{
                start = [int]$rangeMatch.Groups[1].Value
                end = [int]$rangeMatch.Groups[2].Value
                source = '01_CONTINUIDADE/PROMPT_PROXIMO_PROCESSO.txt'
            }
            if ($result.next_cycle.end - $result.next_cycle.start -ne 4) {
                $errors.Add('NEXT_CYCLE_NOT_FIVE_LOTS')
            }
            if ($result.next_cycle.start -ne $ExpectedLastLot + 1) {
                $errors.Add("NEXT_CYCLE_NOT_CONTIGUOUS:esperado $($ExpectedLastLot + 1)")
            }
        }

        $manifest = Get-ZipText -Zip $zip -Name '01_CONTINUIDADE/MANIFESTO_SHA256.json' | ConvertFrom-Json
        $manifestEntries = @($manifest.arquivos)
        $result.manifest.entries = $manifestEntries.Count
        if ((Get-ObjectValue -Object $manifest -Names @('pacote')).ToUpperInvariant() -notmatch "LOTE$ExpectedLastLot") {
            $errors.Add("MANIFEST_PACKAGE_NAME_MISMATCH:esperado LOTE$ExpectedLastLot")
        }
        $manifestPaths = @($manifestEntries | ForEach-Object { Get-ObjectValue -Object $_ -Names @('arquivo', 'path', 'name') })
        if ((@($manifestPaths | Sort-Object -Unique)).Count -ne $manifestPaths.Count) { $errors.Add('MANIFEST_DUPLICATE_PATH') }
        foreach ($manifestEntry in $manifestEntries) {
            $manifestPath = Get-ObjectValue -Object $manifestEntry -Names @('arquivo', 'path', 'name')
            $expectedHash = (Get-ObjectValue -Object $manifestEntry -Names @('sha256', 'sha256_hash')).ToLowerInvariant()
            $expectedSizeText = Get-ObjectValue -Object $manifestEntry -Names @('tamanho_bytes', 'size', 'length')
            $zipEntry = $zip.GetEntry($manifestPath)
            if ($null -eq $zipEntry) {
                $errors.Add("MANIFEST_ENTRY_MISSING:$manifestPath")
                continue
            }
            $actualHash = Get-ZipEntryHash -Entry $zipEntry
            $actualSize = [int64]$zipEntry.Length
            $result.manifest.checked++
            if ($expectedHash -and $expectedHash -ne $actualHash) {
                $errors.Add("MANIFEST_HASH_MISMATCH:$manifestPath")
                $result.manifest.mismatches += $manifestPath
            }
            if ($expectedSizeText -and [int64]$expectedSizeText -ne $actualSize) {
                $errors.Add("MANIFEST_SIZE_MISMATCH:$manifestPath")
                $result.manifest.mismatches += $manifestPath
            }
        }
        foreach ($requiredPath in $required) {
            if ($requiredPath -ne '01_CONTINUIDADE/MANIFESTO_SHA256.json' -and $requiredPath -notin $manifestPaths) {
                $errors.Add("MANIFEST_REQUIRED_FILE_NOT_COVERED:$requiredPath")
            }
        }

        $jsonData = Get-ZipText -Zip $zip -Name $jsonName | ConvertFrom-Json
        $fichas = @($jsonData.fichas)
        $jsonIds = @($fichas | ForEach-Object { (Get-ObjectValue -Object $_ -Names @('id', 'ID')).Trim().ToUpperInvariant() } | Where-Object { $_ })
        $auditRows = Get-CsvRowsFromText -Text (Get-ZipText -Zip $zip -Name $auditName)
        $imageRows = Get-CsvRowsFromText -Text (Get-ZipText -Zip $zip -Name $imageCsvName)
        $auditIds = @($auditRows | ForEach-Object { (Get-ObjectValue -Object $_ -Names @('ID', 'id')).Trim().ToUpperInvariant() } | Where-Object { $_ })
        $imageIds = @($imageRows | ForEach-Object { (Get-ObjectValue -Object $_ -Names @('ID', 'id')).Trim().ToUpperInvariant() } | Where-Object { $_ })
        $duplicateSets = @(
            (Get-DuplicateValues -Values $jsonIds),
            (Get-DuplicateValues -Values $auditIds),
            (Get-DuplicateValues -Values $imageIds)
        )
        $duplicates = @($duplicateSets | Where-Object { $_ })
        if ($jsonIds.Count -ne 607 -or $auditIds.Count -ne 607 -or $imageIds.Count -ne 607) { $errors.Add('ID_COUNT_NOT_607') }
        if ($duplicates.Count -gt 0) { $errors.Add("ID_DUPLICATES:$($duplicates -join ',')") }
        $jsonSet = ($jsonIds | Sort-Object -Unique) -join '|'
        if ($jsonSet -ne (($auditIds | Sort-Object -Unique) -join '|') -or $jsonSet -ne (($imageIds | Sort-Object -Unique) -join '|')) {
            $errors.Add('ID_SETS_MISMATCH_JSON_AUDIT_IMAGES')
        }
        $result.counts.ids = $jsonIds.Count

        $completeRows = @($auditRows | Where-Object {
            $flag = (Get-ObjectValue -Object $_ -Names @('Ficha_mecanica_completa', 'ficha_mecanica_completa')).Trim().ToLowerInvariant()
            $flag -match '^(sim|true|1|completa)$'
        })
        $verifiedImageRows = @($imageRows | Where-Object {
            $direct = (Get-ObjectValue -Object $_ -Names @('URL_imagem_direta', 'url_imagem_direta')).Trim()
            $status = Get-ObjectValue -Object $_ -Names @('Status_verificacao', 'status_verificacao')
            $mime = Get-ObjectValue -Object $_ -Names @('Tipo_conteudo', 'tipo_conteudo')
            $dimensions = Get-ObjectValue -Object $_ -Names @('Dimensoes', 'dimensoes')
            $visual = Get-ObjectValue -Object $_ -Names @('Correspondencia_visual', 'correspondencia_visual')
            $direct -and $status -match '(?i)URL direta carregada' -and $mime -and $dimensions -and $visual -and $visual -notmatch '(?i)não confirmada|nao confirmada'
        })
        $result.counts.complete_fichas = $completeRows.Count
        $result.counts.verified_images = $verifiedImageRows.Count
        if ($jsonData.total -ne 607 -or $fichas.Count -ne 607) { $errors.Add('JSON_TOTAL_NOT_607') }
        $report = Get-ZipText -Zip $zip -Name $reportName
        if ($report -notmatch '(?i)607') { $errors.Add('REPORT_TOTAL_NOT_607') }
        if (-not (Test-ReportCount -Report $report -Count $completeRows.Count -Pattern '(?i)ficha|mecânica|mecanica|complet')) { $errors.Add('REPORT_COMPLETE_COUNT_MISMATCH') }
        if (-not (Test-ReportCount -Report $report -Count $verifiedImageRows.Count -Pattern '(?i)imagem|URL direta')) { $errors.Add('REPORT_IMAGE_COUNT_MISMATCH') }
        if (-not (Test-DocxEntry -OuterZip $zip -Name $fichasDocxName)) { $errors.Add('DOCX_FICHAS_INVALID') }
        if (-not (Test-DocxEntry -OuterZip $zip -Name $imagesDocxName)) { $errors.Add('DOCX_IMAGES_INVALID') }
        if (-not (Test-NestedZipEntry -OuterZip $zip -Name $nestedZipName)) { $errors.Add('OUTPUT_ZIP_INVALID') }
        if ($result.next_cycle -and $result.next_cycle.start -gt 607) { $errors.Add('NEXT_CYCLE_AFTER_CAMPAIGN_TARGET') }
        $result.last_lot = $ExpectedLastLot
    }
    catch {
        $errors.Add("PACKAGE_AUDIT_EXCEPTION:$($_.Exception.Message)")
    }
    finally {
        $zip.Dispose()
    }

    $result.errors = @($errors | Select-Object -Unique)
    $result.pass = ($result.errors.Count -eq 0)
    if ($result.pass) {
        $result.code = 'PACKAGE_VALID'
        $result.detail = 'Pacote, manifesto, IDs, contagens, documentos e ZIP interno passaram na auditoria.'
    }
    else {
        $result.code = [string]$result.errors[0]
        $result.detail = ($result.errors -join '; ')
    }
    return [pscustomobject]$result
}

function Find-CandidatePackage {
    $roots = @('D:\Repos', $script:SupervisorRoot, (Get-Location).Path) | Select-Object -Unique
    $candidates = [Collections.Generic.List[string]]::new()
    foreach ($root in $roots) {
        if (-not (Test-Path -LiteralPath $root -PathType Container)) { continue }
        Get-ChildItem -LiteralPath $root -Recurse -File -Filter '*SRD_PACOTE_CONTINUIDADE_LOTE20_2026-10-10*.zip' -ErrorAction SilentlyContinue |
            ForEach-Object { $candidates.Add($_.FullName) }
    }
    return @($candidates.ToArray() | Sort-Object -Unique)
}

function Get-CodexExecutable {
    # On Windows `codex` normally resolves first to codex.ps1, which is a
    # signed resolver but not a native process image. Resolve the native
    # signed Desktop runtime so ProcessStartInfo can launch it directly.
    $native = Get-Command codex.exe -ErrorAction Stop
    if ($native.CommandType -ne 'Application') { throw 'CODEX_EXECUTABLE_NOT_FOUND' }
    $path = if ($native.Source) { $native.Source } else { $native.Path }
    if ([IO.Path]::GetExtension($path).ToLowerInvariant() -ne '.exe') {
        throw "CODEX_LAUNCHER_UNSUPPORTED:$path"
    }
    $signature = Get-AuthenticodeSignature -LiteralPath $path
    if ($signature.Status -ne 'Valid' -or $signature.SignerCertificate.Subject -notmatch '(?:^|, )CN="OpenAI OpCo, LLC"(?:,|$)') {
        throw "CODEX_RUNTIME_SIGNATURE_INVALID:$path"
    }
    return $path
}

function Invoke-CliCapture {
    param(
        [Parameter(Mandatory)][string]$FilePath,
        [Parameter(Mandatory)][string[]]$Arguments
    )
    $start = [Diagnostics.ProcessStartInfo]::new()
    $start.FileName = $FilePath
    $start.UseShellExecute = $false
    $start.CreateNoWindow = $true
    $start.RedirectStandardOutput = $true
    $start.RedirectStandardError = $true
    foreach ($argument in $Arguments) { [void]$start.ArgumentList.Add($argument) }
    $process = [Diagnostics.Process]::new()
    $process.StartInfo = $start
    if (-not $process.Start()) { throw 'CLI_START_FAILED' }
    $outTask = $process.StandardOutput.ReadToEndAsync()
    $errTask = $process.StandardError.ReadToEndAsync()
    $process.WaitForExit()
    return [pscustomobject]@{
        exit_code = $process.ExitCode
        stdout = Redact-Secrets $outTask.Result
        stderr = Redact-Secrets $errTask.Result
    }
}

function Test-CodexCapabilities {
    $codexPath = Get-CodexExecutable
    $version = Invoke-CliCapture -FilePath $codexPath -Arguments @('--version')
    $help = Invoke-CliCapture -FilePath $codexPath -Arguments @('exec', '--help')
    if ($version.exit_code -ne 0) { throw "CODEX_VERSION_FAILED:$($version.stderr)" }
    if ($help.exit_code -ne 0) { throw "CODEX_EXEC_HELP_FAILED:$($help.stderr)" }
    $requiredOptions = @('-C', '-s', '--json', '-o', '--add-dir')
    $missing = @($requiredOptions | Where-Object { $help.stdout -notmatch "(?m)(^|\s)$([regex]::Escape($_))(\s|,|$)" })
    if ($missing.Count -gt 0) { throw "CODEX_CAPABILITY_MISSING:$($missing -join ',')" }
    return [ordered]@{
        path = $codexPath
        version = ($version.stdout.Trim() -split '\r?\n' | Select-Object -First 1)
        help_options = @('-C', '-s', '--json', '-o', '--add-dir')
        model = $Model
        reasoning_effort = $ReasoningEffort
    }
}

function Test-TrustedGitWorkdir {
    param([Parameter(Mandatory)][string]$Path)
    if (-not (Test-Path -LiteralPath $Path -PathType Container)) { throw 'WORKDIR_NOT_FOUND' }
    $top = (& git -C $Path rev-parse --show-toplevel 2>$null | Out-String).Trim()
    if ($LASTEXITCODE -ne 0 -or -not $top) { throw 'WORKDIR_NOT_TRUSTED_GIT_REPOSITORY' }
    return $top
}

function Get-DispatchKey {
    param(
        [Parameter(Mandatory)][int]$StartLot,
        [Parameter(Mandatory)][int]$EndLot,
        [Parameter(Mandatory)][string]$PackageSha256
    )
    return "$CampaignId|$StartLot-$EndLot|$($PackageSha256.ToLowerInvariant())"
}

function Get-NextCycleFromValidation {
    param([Parameter(Mandatory)]$Validation)
    if ($null -eq $Validation.next_cycle) { return $null }
    return [ordered]@{
        start = [int]$Validation.next_cycle.start
        end = [int]$Validation.next_cycle.end
    }
}

function New-CyclePrompt {
    param(
        [Parameter(Mandatory)]$State,
        [Parameter(Mandatory)]$Cycle,
        [Parameter(Mandatory)][string]$PackagePathForPrompt,
        [Parameter(Mandatory)][string]$PackageSha256,
        [Parameter(Mandatory)][string]$OutputDirectory,
        [Parameter(Mandatory)][string]$WorkspaceRoot
    )
    $complete = if ($null -eq $State.counts.complete_fichas) { 'desconhecida' } else { $State.counts.complete_fichas }
    $images = if ($null -eq $State.counts.verified_images) { 'desconhecida' } else { $State.counts.verified_images }
    $pythonHint = if (Test-Path -LiteralPath $script:BundledPythonPath) { '$env:SRD_BUNDLED_PYTHON' } else { 'python' }
    return @"
Você é uma execução independente do Codex CLI iniciada pelo supervisor local da campanha SRD Card Game 607.

MODELO: $Model
RACIOCÍNIO: $ReasoningEffort
NÃO use `codex exec resume`, não abra nem simule conversa do ChatGPT e não use automação de navegador para criar conversa.

Campanha: $CampaignId
Pacote de continuidade-base validado: $PackagePathForPrompt
SHA-256 do pacote-base: $PackageSha256
Intervalo desta execução: ciclo operacional $($Cycle.start)–$($Cycle.end) (exatamente cinco posições consecutivas; selecione as cinco próximas fichas pendentes do estado confirmado, sem tratar números históricos de lote como novos IDs).
Contagem confirmada antes do ciclo: fichas completas=$complete; imagens diretas verificadas=$images.
Diretório obrigatório de saída desta execução: $OutputDirectory

Se precisar executar Python para construir DOCX ou validar dados, use exatamente $pythonHint e confirme que `import docx` funciona. Não use pip, não instale componentes e não substitua DOCX por arquivo inválido.

Use o estado e os construtores existentes no pacote. O helper local de empacotamento, quando aplicável, é `$WorkspaceRoot\New-SRDOperationalContinuationPackage.ps1`; a saída final deve ser um pacote único `SRD_PACOTE_CONTINUIDADE_LOTE$($Cycle.end)_<data>.zip` dentro do diretório do ciclo, preservando o pacote-base recebido.

Leia o pacote-base e as instruções do projeto. Derive quantidade de registros, limites e seleção do estado real; não invente limites, IDs, atributos, valores, ações, CDs, URLs, status HTTP ou confirmações. Preserve exatamente os 607 IDs válidos e os 28 homebrews autorais excluídos; mantenha os homebrews publicados por Kobold Press, EN Publishing/A5E e MCDM quando forem válidos.

Execute apenas os lotes atribuídos a esta execução. Gere os documentos, JSON, CSVs, relatório, manifesto SHA-256 e ZIP versionado exigidos pelo projeto. Audite IDs sem duplicatas, identidade/publicação/editora/edição/sistema/variante/porte/tipo/ND, mecânica e referências rastreáveis, URLs de imagem somente após verificação configurada, contagens entre formatos e integridade dos ZIPs. Registre pendências honestamente.

Ao finalizar, deixe no diretório obrigatório um pacote de continuidade cujo nome contenha o último ciclo realmente processado (por exemplo, LOTE$($Cycle.end)), sem sobrescrever pacotes anteriores. O pacote deve conter 01_CONTINUIDADE, 02_SAIDA_<versão>, 03_CONSTRUTOR, 04_INSUMOS e, a partir do segundo ciclo, 00_PACOTE_BASE com o pacote validado anterior. Inclua no prompt de continuidade as cinco próximas posições consecutivas. Se execução, preflight, credential broker, auditoria, empacotamento ou ferramenta de pesquisa bloquear, retorne código de saída diferente de zero ou deixe o bloqueio explicitamente documentado; não converta bloqueio em sucesso.

Não grave credenciais, tokens ou segredos em prompts, arquivos de estado ou logs. O supervisor só avançará depois de validar este pacote e suas hashes.
"@
}

function Find-CyclePackage {
    param(
        [Parameter(Mandatory)][string]$OutputDirectory,
        [Parameter(Mandatory)][int]$EndLot,
        [Parameter(Mandatory)][datetime]$StartedAt
    )
    if (-not (Test-Path -LiteralPath $OutputDirectory -PathType Container)) { return $null }
    $pattern = "*LOTE$EndLot*.zip"
    $candidates = @(Get-ChildItem -LiteralPath $OutputDirectory -Recurse -File -Filter $pattern -ErrorAction SilentlyContinue |
        Where-Object { $_.LastWriteTimeUtc -ge $StartedAt.ToUniversalTime().AddSeconds(-2) } |
        Sort-Object LastWriteTimeUtc -Descending)
    if ($candidates.Count -eq 0) { return $null }
    return $candidates[0].FullName
}

function Set-BlockedState {
    param(
        [Parameter(Mandatory)]$State,
        [Parameter(Mandatory)][string]$Code,
        [Parameter(Mandatory)][string]$Detail
    )
    $State.status = 'BLOCKED'
    $State.last_error = [ordered]@{ code = $Code; detail = Redact-Secrets $Detail; at = Get-UtcTimestamp }
    Save-CampaignState -State $State
    Add-HistoryEvent -Event 'BLOCKED' -Data $State.last_error
    return $State
}

function Apply-ValidatedCycleTransition {
    [OutputType([pscustomobject])]
    param(
        [Parameter(Mandatory)]$State,
        [Parameter(Mandatory)][int]$CycleStart,
        [Parameter(Mandatory)][int]$CycleEnd,
        [Parameter(Mandatory)][string]$PackageSha256,
        [Parameter(Mandatory)][bool]$AuditPassed,
        [Parameter(Mandatory)][int]$CompleteFichas,
        [Parameter(Mandatory)][int]$VerifiedImages,
        [Parameter(Mandatory)][int]$TargetTotal,
        [AllowNull()][int]$NextStart,
        [AllowNull()][int]$NextEnd,
        [string]$FailureCode = ''
    )
    $dispatchKey = Get-DispatchKey -StartLot $CycleStart -EndLot $CycleEnd -PackageSha256 $PackageSha256
    # PENDING/STARTED is the durable reservation for the cycle currently being
    # reconciled. Only SUCCEEDED is a completed duplicate.
    $known = @($State.dispatches | Where-Object { $_.idempotency_key -eq $dispatchKey -and $_.status -eq 'SUCCEEDED' })
    if ($known.Count -gt 0) {
        return [pscustomobject]@{ action = 'DUPLICATE_IGNORED'; dispatch_key = $dispatchKey; state = $State }
    }
    if ($State.status -in @('COMPLETED', 'CANCELLED', 'BLOCKED')) {
        return [pscustomobject]@{ action = 'TERMINAL_NOOP'; dispatch_key = $dispatchKey; state = $State }
    }
    if (-not $AuditPassed) {
        $State.status = 'BLOCKED'
        $State.next_cycle = $null
        $State.last_error = [ordered]@{ code = if ($FailureCode) { $FailureCode } else { 'AUDIT_FAILED' }; detail = 'O ciclo não passou na auditoria; o checkpoint foi preservado e não há próximo despacho.'; at = Get-UtcTimestamp }
        return [pscustomobject]@{ action = 'BLOCKED'; dispatch_key = $dispatchKey; state = $State }
    }
    $State.counts.complete_fichas = $CompleteFichas
    $State.counts.verified_images = $VerifiedImages
    $State.target.total = $TargetTotal
    $State.target.complete_fichas = $TargetTotal
    $State.target.verified_images = $TargetTotal
    $currentDispatch = @($State.dispatches | Where-Object { $_.idempotency_key -eq $dispatchKey })
    if ($currentDispatch.Count -gt 0) {
        $State.dispatches = @($State.dispatches | ForEach-Object {
            if ($_.idempotency_key -eq $dispatchKey) {
                $_.status = 'SUCCEEDED'
                $completedAt = Get-UtcTimestamp
                if ($null -ne $_.PSObject.Properties['completed_at']) { $_.completed_at = $completedAt }
                else { $_ | Add-Member -NotePropertyName completed_at -NotePropertyValue $completedAt }
            }
            $_
        })
    }
    else {
        $State.dispatches += [pscustomobject]([ordered]@{ idempotency_key = $dispatchKey; cycle = "$CycleStart-$CycleEnd"; status = 'SUCCEEDED'; at = Get-UtcTimestamp })
    }
    if ($CompleteFichas -ge $TargetTotal -and $VerifiedImages -ge $TargetTotal) {
        $State.status = 'COMPLETED'
        $State.next_cycle = $null
        return [pscustomobject]@{ action = 'COMPLETED'; dispatch_key = $dispatchKey; state = $State }
    }
    if ($null -eq $NextStart -or $null -eq $NextEnd -or $NextEnd - $NextStart -ne 4 -or $NextStart -ne $CycleEnd + 1) {
        $State.status = 'BLOCKED'
        $State.next_cycle = $null
        $State.last_error = [ordered]@{ code = 'NEXT_CYCLE_INVALID'; detail = 'O pacote validado não declarou um próximo intervalo contíguo de cinco lotes.'; at = Get-UtcTimestamp }
        return [pscustomobject]@{ action = 'BLOCKED'; dispatch_key = $dispatchKey; state = $State }
    }
    $State.next_cycle = [ordered]@{ start = $NextStart; end = $NextEnd }
    $State.status = 'READY_TO_DISPATCH'
    $State.last_error = $null
    return [pscustomobject]@{ action = 'READY_TO_DISPATCH'; dispatch_key = $dispatchKey; state = $State }
}

function Register-DispatchIfNeeded {
    param(
        [Parameter(Mandatory)]$State,
        [Parameter(Mandatory)][int]$CycleStart,
        [Parameter(Mandatory)][int]$CycleEnd,
        [Parameter(Mandatory)][string]$PackageSha256
    )
    $key = Get-DispatchKey -StartLot $CycleStart -EndLot $CycleEnd -PackageSha256 $PackageSha256
    if ($State.status -in @('COMPLETED', 'CANCELLED', 'BLOCKED')) {
        return [pscustomobject]@{ created = $false; reason = 'TERMINAL_STATE'; idempotency_key = $key }
    }
    $existing = @($State.dispatches | Where-Object { $_.idempotency_key -eq $key -and $_.status -in @('PENDING', 'STARTED', 'SUCCEEDED') })
    if ($existing.Count -gt 0) {
        return [pscustomobject]@{ created = $false; reason = 'ALREADY_REGISTERED'; idempotency_key = $key }
    }
    $State.dispatches += [pscustomobject]([ordered]@{ idempotency_key = $key; cycle = "$CycleStart-$CycleEnd"; status = 'PENDING'; at = Get-UtcTimestamp })
    return [pscustomobject]@{ created = $true; reason = 'REGISTERED'; idempotency_key = $key }
}

function Invoke-SimulationTransition {
    param(
        [Parameter(Mandatory)][ValidateSet('normal', 'early-complete', 'failure')][string]$Scenario,
        [int]$Cycles = 2
    )
    $state = New-CampaignState
    $state.status = 'READY_TO_DISPATCH'
    $state.package_base = [ordered]@{ path = 'SIMULATED://LOTE20'; sha256 = ('0' * 64); last_lot = 20 }
    $state.target = [ordered]@{ total = 607; complete_fichas = 607; verified_images = 607 }
    $state.counts = [ordered]@{ ids = 607; complete_fichas = 185; verified_images = 21 }
    $state.next_cycle = [ordered]@{ start = 21; end = 25 }
    $events = [Collections.Generic.List[object]]::new()
    for ($index = 0; $index -lt $Cycles; $index++) {
        if ($null -eq $state.next_cycle -or $state.status -in @('COMPLETED', 'BLOCKED', 'CANCELLED')) { break }
        $cycle = $state.next_cycle
        $auditPassed = $Scenario -ne 'failure'
        $complete = if ($Scenario -eq 'early-complete') { 607 } else { 185 + (($index + 1) * 5) }
        $images = if ($Scenario -eq 'early-complete') { 607 } else { 21 + (($index + 1) * 5) }
        $nextStart = [int]$cycle.end + 1
        $nextEnd = $nextStart + 4
        $transition = Apply-ValidatedCycleTransition -State $state -CycleStart $cycle.start -CycleEnd $cycle.end -PackageSha256 (('{0:x64}' -f ($index + 1)) * 8).Substring(0, 64) -AuditPassed $auditPassed -CompleteFichas $complete -VerifiedImages $images -TargetTotal 607 -NextStart $nextStart -NextEnd $nextEnd -FailureCode 'SIMULATED_AUDIT_FAILED'
        $state = $transition.state
        $events.Add([ordered]@{ cycle = "$($cycle.start)-$($cycle.end)"; action = $transition.action; status = $state.status })
        if ($transition.action -eq 'READY_TO_DISPATCH') {
            $registration = Register-DispatchIfNeeded -State $state -CycleStart $nextStart -CycleEnd $nextEnd -PackageSha256 (('{0:x64}' -f ($index + 2)) * 8).Substring(0, 64)
            $events.Add([ordered]@{ cycle = "$nextStart-$nextEnd"; dispatch = $registration.reason })
        }
    }
    return [pscustomobject]@{ state = $state; events = @($events) }
}

function Invoke-Simulation {
    $simulation = Invoke-SimulationTransition -Scenario $SimulationScenario -Cycles $SimulationCycles
    $simulationPath = Join-Path $script:StateDir ("simulation-{0}-{1}.json" -f $SimulationScenario, ([guid]::NewGuid().ToString('N')))
    Write-AtomicJson -Path $simulationPath -Value ([ordered]@{ mode = 'simulation'; scenario = $SimulationScenario; created_at = Get-UtcTimestamp; result = $simulation })
    [pscustomobject]@{
        mode = 'simulation'
        scenario = $SimulationScenario
        state_path = $simulationPath
        final_status = $simulation.state.status
        next_cycle = $simulation.state.next_cycle
        events = $simulation.events
        real_research_started = $false
    } | ConvertTo-Json -Depth 20
}

function Assert-Test {
    param(
        [Parameter(Mandatory)][bool]$Condition,
        [Parameter(Mandatory)][string]$Message
    )
    if (-not $Condition) { throw "SELFTEST_FAILED:$Message" }
}

function Invoke-SelfTest {
    $results = [Collections.Generic.List[object]]::new()
    $normal = Invoke-SimulationTransition -Scenario normal -Cycles 1
    Assert-Test ($normal.events[0].action -eq 'READY_TO_DISPATCH') '21-25 não avançou para despacho pronto'
    Assert-Test ($normal.state.next_cycle.start -eq 26 -and $normal.state.next_cycle.end -eq 30) 'próximo ciclo normal não é 26-30'
    $results.Add([ordered]@{ test = 'normal-21-25-to-26-30'; result = 'PASS' })

    $early = Invoke-SimulationTransition -Scenario early-complete -Cycles 2
    Assert-Test ($early.state.status -eq 'COMPLETED' -and $null -eq $early.state.next_cycle) 'conclusão antecipada iniciou ciclo seguinte'
    $results.Add([ordered]@{ test = 'early-completion-607-607'; result = 'PASS' })

    $failure = Invoke-SimulationTransition -Scenario failure -Cycles 2
    Assert-Test ($failure.state.status -eq 'BLOCKED' -and $null -eq $failure.state.next_cycle) 'auditoria falha avançou ciclo'
    $results.Add([ordered]@{ test = 'audit-failure-no-advance'; result = 'PASS' })

    $state = New-CampaignState
    $state.status = 'READY_TO_DISPATCH'
    $state.package_base.sha256 = 'a' * 64
    $first = Register-DispatchIfNeeded -State $state -CycleStart 21 -CycleEnd 25 -PackageSha256 $state.package_base.sha256
    $second = Register-DispatchIfNeeded -State $state -CycleStart 21 -CycleEnd 25 -PackageSha256 $state.package_base.sha256
    Assert-Test ($first.created -and -not $second.created -and @($state.dispatches).Count -eq 1) 'retry do mesmo evento duplicou despacho'
    $results.Add([ordered]@{ test = 'retry-idempotency'; result = 'PASS' })

    $recovered = $state | ConvertTo-Json -Depth 20 | ConvertFrom-Json
    $afterRestart = Register-DispatchIfNeeded -State $recovered -CycleStart 21 -CycleEnd 25 -PackageSha256 $state.package_base.sha256
    Assert-Test (-not $afterRestart.created -and @($recovered.dispatches).Count -eq 1) 'reinício entre checkpoint e despacho duplicou'
    $results.Add([ordered]@{ test = 'restart-between-checkpoint-and-dispatch'; result = 'PASS' })

    $simultaneous = $state | ConvertTo-Json -Depth 20 | ConvertFrom-Json
    $one = Register-DispatchIfNeeded -State $simultaneous -CycleStart 26 -CycleEnd 30 -PackageSha256 ('b' * 64)
    $two = Register-DispatchIfNeeded -State $simultaneous -CycleStart 26 -CycleEnd 30 -PackageSha256 ('b' * 64)
    Assert-Test ($one.created -and -not $two.created) 'eventos simultâneos não foram deduplicados'
    $results.Add([ordered]@{ test = 'simultaneous-events'; result = 'PASS' })

    foreach ($blockedCode in @('PREFLIGHT_BLOCKED', 'CREDENTIAL_BROKER_REQUIRED')) {
        $blocked = New-CampaignState
        $blocked.status = 'BLOCKED'
        $blocked.last_error = [ordered]@{ code = $blockedCode; detail = 'simulado'; at = Get-UtcTimestamp }
        $registration = Register-DispatchIfNeeded -State $blocked -CycleStart 26 -CycleEnd 30 -PackageSha256 ('c' * 64)
        Assert-Test (-not $registration.created) "$blockedCode permitiu despacho"
        $results.Add([ordered]@{ test = "blocked-$($blockedCode.ToLowerInvariant())-no-next"; result = 'PASS' })
    }

    foreach ($terminalStatus in @('COMPLETED', 'CANCELLED', 'BLOCKED')) {
        $terminal = New-CampaignState
        $terminal.status = $terminalStatus
        $registration = Register-DispatchIfNeeded -State $terminal -CycleStart 26 -CycleEnd 30 -PackageSha256 ('d' * 64)
        Assert-Test (-not $registration.created) "$terminalStatus permitiu despacho"
        $results.Add([ordered]@{ test = "terminal-$($terminalStatus.ToLowerInvariant())-no-next"; result = 'PASS' })
    }

    $lock = New-LockHandle
    try {
        $secondLockRejected = $false
        try { $unusedLock = New-LockHandle }
        catch { $secondLockRejected = $_.Exception.Message -match 'CAMPAIGN_LOCK_HELD' }
        Assert-Test $secondLockRejected 'segundo supervisor conseguiu adquirir o lock'
    }
    finally { Release-LockHandle -Handle $lock }
    Assert-Test (-not (Test-Path -LiteralPath $script:LockPath)) 'lock de teste não foi liberado'
    $results.Add([ordered]@{ test = 'campaign-lock'; result = 'PASS' })

    $testPath = Join-Path $script:StateDir ("selftest-{0}.json" -f ([guid]::NewGuid().ToString('N')))
    Write-AtomicJson -Path $testPath -Value ([ordered]@{ mode = 'selftest'; at = Get-UtcTimestamp; results = @($results) })
    [pscustomobject]@{
        mode = 'selftest'
        result = 'PASS'
        test_count = $results.Count
        evidence_path = $testPath
        tests = @($results)
        codex_invoked = $false
        real_research_started = $false
    } | ConvertTo-Json -Depth 20
}

function Initialize-FromPackage {
    param(
        [Parameter(Mandatory)][string]$Path,
        [Parameter(Mandatory)]$State,
        [int]$ExpectedLastLot = 20,
        [int]$RequiredBaseLot = 20
    )
    $validation = Test-ContinuityPackage -Path $Path -ExpectedLastLot $ExpectedLastLot -RequiredBaseLot $RequiredBaseLot
    $State.package_base = [ordered]@{ path = $Path; sha256 = $validation.sha256; last_lot = $validation.last_lot; required_base_lot = $RequiredBaseLot }
    if ($validation.counts) { $State.counts = $validation.counts }
    $State.target.total = 607
    $State.target.complete_fichas = 607
    $State.target.verified_images = 607
    if ($validation.next_cycle) { $State.next_cycle = [ordered]@{ start = $validation.next_cycle.start; end = $validation.next_cycle.end } }
    return [pscustomobject]@{ state = $State; validation = $validation }
}

function Invoke-Prepare {
    $state = Read-CampaignState
    if ($null -eq $state) { $state = New-CampaignState }
    $path = $PackagePath
    if (-not $path) {
        $candidates = @(Find-CandidatePackage)
        if ($candidates.Count -eq 1) { $path = $candidates[0] }
        elseif ($candidates.Count -gt 1) {
            $state = Set-BlockedState -State $state -Code 'PACKAGE_AMBIGUOUS' -Detail ($candidates -join '; ')
            [pscustomobject]@{ status = $state.status; code = 'PACKAGE_AMBIGUOUS'; candidates = $candidates; real_research_started = $false } | ConvertTo-Json -Depth 10
            return
        }
    }
    if (-not $path) {
        $state = Set-BlockedState -State $state -Code 'PACKAGE_NOT_FOUND' -Detail 'Nenhum SRD_PACOTE_CONTINUIDADE_LOTE20_2026-10-10.zip foi localizado em D:\Repos, no supervisor ou no diretório atual.'
        [pscustomobject]@{ status = $state.status; code = 'PACKAGE_NOT_FOUND'; real_research_started = $false } | ConvertTo-Json -Depth 10
        return
    }
    $initialized = Initialize-FromPackage -Path ([IO.Path]::GetFullPath($path)) -State $state -ExpectedLastLot $ExpectedLastLot -RequiredBaseLot $RequiredBaseLot
    $state = $initialized.state
    if ($initialized.validation.pass) {
        $state.status = 'READY_TO_DISPATCH'
        $state.last_error = $null
        Save-CampaignState -State $state
        Add-HistoryEvent -Event 'PACKAGE_VALIDATED' -Data $initialized.validation
    }
    else {
        $state.status = 'BLOCKED'
        $state.last_error = [ordered]@{ code = $initialized.validation.code; detail = $initialized.validation.detail; at = Get-UtcTimestamp }
        Save-CampaignState -State $state
        Add-HistoryEvent -Event 'PACKAGE_REJECTED' -Data ([ordered]@{ code = $initialized.validation.code; detail = $initialized.validation.detail; sha256 = $initialized.validation.sha256 })
    }
    [pscustomobject]@{
        status = $state.status
        code = $initialized.validation.code
        detail = $initialized.validation.detail
        package = $initialized.validation
        state_path = $script:StatePath
        real_research_started = $false
    } | ConvertTo-Json -Depth 30
}

function Invoke-CodexCycle {
    param(
        [Parameter(Mandatory)]$State,
        [Parameter(Mandatory)]$Cycle,
        [Parameter(Mandatory)][string]$ValidatedPackagePath,
        [Parameter(Mandatory)][string]$ValidatedPackageSha256,
        [Parameter(Mandatory)][string]$TrustedWorkdir,
        [Parameter(Mandatory)]$CodexCapability
    )
    $cycleId = "cycle-$($Cycle.start)-$($Cycle.end)-$([guid]::NewGuid().ToString('N').Substring(0, 12))"
    $cycleDir = Join-Path $script:RunsDir $cycleId
    Ensure-Directory -Path $cycleDir
    $outputDirectory = Join-Path $TrustedWorkdir ("SRD_CYCLES\$($Cycle.start)-$($Cycle.end)")
    Ensure-Directory -Path $outputDirectory
    $promptPath = Join-Path $cycleDir 'prompt.txt'
    $stdoutPath = Join-Path $cycleDir 'stdout.jsonl'
    $stderrPath = Join-Path $cycleDir 'stderr.log'
    $lastMessagePath = Join-Path $cycleDir 'last-message.txt'
    $prompt = New-CyclePrompt -State $State -Cycle $Cycle -PackagePathForPrompt $ValidatedPackagePath -PackageSha256 $ValidatedPackageSha256 -OutputDirectory $outputDirectory -WorkspaceRoot $TrustedWorkdir
    Write-AtomicText -Path $promptPath -Text (Redact-Secrets $prompt)
    $key = Get-DispatchKey -StartLot $Cycle.start -EndLot $Cycle.end -PackageSha256 $ValidatedPackageSha256
    $existing = @($State.dispatches | Where-Object { $_.idempotency_key -eq $key })
    if ($existing.Count -gt 0 -and $existing[0].status -in @('STARTED', 'SUCCEEDED')) {
        return [pscustomobject]@{ success = $false; code = 'DISPATCH_DUPLICATE_PREVENTED'; detail = 'A mesma chave de despacho já foi iniciada/concluída.'; cycle_id = $cycleId }
    }
    $attempt = @($State.attempts | Where-Object { $_.cycle -eq "$($Cycle.start)-$($Cycle.end)" }).Count + 1
    $State.status = 'RUNNING'
    $State.current_cycle = [ordered]@{
        cycle_id = $cycleId
        start = $Cycle.start
        end = $Cycle.end
        attempt = $attempt
        idempotency_key = $key
        pid = $null
        started_at = Get-UtcTimestamp
        prompt_path = $promptPath
        stdout_path = $stdoutPath
        stderr_path = $stderrPath
        last_message_path = $lastMessagePath
        output_directory = $outputDirectory
        package_base_sha256 = $ValidatedPackageSha256
    }
    $State.attempts += [pscustomobject]([ordered]@{ cycle = "$($Cycle.start)-$($Cycle.end)"; attempt = $attempt; cycle_id = $cycleId; idempotency_key = $key; started_at = $State.current_cycle.started_at; status = 'STARTED' })
    if ($existing.Count -eq 0) {
        $State.dispatches += [pscustomobject]([ordered]@{ idempotency_key = $key; cycle = "$($Cycle.start)-$($Cycle.end)"; status = 'STARTED'; cycle_id = $cycleId; at = Get-UtcTimestamp })
    }
    else {
        $State.dispatches = @($State.dispatches | ForEach-Object {
            if ($_.idempotency_key -eq $key) {
                $_.status = 'STARTED'
                Set-ObjectProperty -Object $_ -Name 'cycle_id' -Value $cycleId
            }
            $_
        })
    }
    Save-CampaignState -State $State
    Add-HistoryEvent -Event 'CYCLE_STARTED' -Data ([ordered]@{ cycle_id = $cycleId; cycle = "$($Cycle.start)-$($Cycle.end)"; idempotency_key = $key; package_sha256 = $ValidatedPackageSha256; prompt_path = $promptPath })

    $startedAt = Get-Date
    $arguments = @('exec', '-C', $TrustedWorkdir, '--add-dir', $TrustedWorkdir, '--add-dir', $script:SupervisorRoot, '-s', 'workspace-write', '--json', '-o', $lastMessagePath, '-m', $Model, '-c', "model_reasoning_effort=$ReasoningEffort", '-')
    $start = [Diagnostics.ProcessStartInfo]::new()
    $start.FileName = $CodexCapability.path
    $start.UseShellExecute = $false
    $start.CreateNoWindow = $true
    $start.RedirectStandardInput = $true
    $start.RedirectStandardOutput = $true
    $start.RedirectStandardError = $true
    $start.StandardInputEncoding = [Text.UTF8Encoding]::new($false)
    $start.StandardOutputEncoding = [Text.UTF8Encoding]::new($false)
    $start.StandardErrorEncoding = [Text.UTF8Encoding]::new($false)
    if (Test-Path -LiteralPath $script:BundledPythonPath) {
        $pythonDirectory = Split-Path -Parent $script:BundledPythonPath
        $start.Environment['SRD_BUNDLED_PYTHON'] = $script:BundledPythonPath
        $start.Environment['Path'] = "$pythonDirectory;$($start.Environment['Path'])"
    }
    foreach ($argument in $arguments) { [void]$start.ArgumentList.Add($argument) }
    $process = [Diagnostics.Process]::new()
    $process.StartInfo = $start
    try {
        if (-not $process.Start()) { throw 'CODEX_START_FAILED' }
        $State.current_cycle.pid = $process.Id
        Save-CampaignState -State $State
        $process.StandardInput.Write($prompt)
        $process.StandardInput.Close()
        $outTask = $process.StandardOutput.ReadToEndAsync()
        $errTask = $process.StandardError.ReadToEndAsync()
        $process.WaitForExit()
        $stdout = Redact-Secrets $outTask.Result
        $stderr = Redact-Secrets $errTask.Result
        Write-AtomicText -Path $stdoutPath -Text $stdout
        Write-AtomicText -Path $stderrPath -Text $stderr
        if (Test-Path -LiteralPath $lastMessagePath) {
            Write-AtomicText -Path $lastMessagePath -Text (Redact-Secrets (Get-Content -Raw -LiteralPath $lastMessagePath))
        }
        $exitCode = $process.ExitCode
        $State.current_cycle.ended_at = Get-UtcTimestamp
        $State.current_cycle.exit_code = $exitCode
        $State.current_cycle.stdout_bytes = ([Text.Encoding]::UTF8.GetByteCount($stdout))
        $State.current_cycle.stderr_bytes = ([Text.Encoding]::UTF8.GetByteCount($stderr))
        if ($exitCode -ne 0) {
            $all = "$stdout`n$stderr"
            $code = if ($all -match '(?i)credential.?broker|required') { 'CREDENTIAL_BROKER_REQUIRED' } elseif ($all -match '(?i)preflight|bootstrap') { 'PREFLIGHT_BLOCKED' } else { 'CODEX_EXEC_FAILED' }
            $State.status = 'BLOCKED'
            $State.last_error = [ordered]@{ code = $code; detail = "codex exec terminou com exit code $exitCode"; at = Get-UtcTimestamp }
            $State.dispatches = @($State.dispatches | ForEach-Object { if ($_.idempotency_key -eq $key) { $_.status = 'FAILED' }; $_ })
            Save-CampaignState -State $State
            Add-HistoryEvent -Event 'CYCLE_FAILED' -Data $State.last_error
            return [pscustomobject]@{ success = $false; code = $code; detail = $State.last_error.detail; cycle_id = $cycleId; exit_code = $exitCode }
        }
        $outputPackage = Find-CyclePackage -OutputDirectory $outputDirectory -EndLot $Cycle.end -StartedAt $startedAt
        if (-not $outputPackage) {
            $all = "$stdout`n$stderr"
            $failureCode = if ($all -match '(?i)helper_unknown_error|setup refresh had errors|failed to write file|failed to create unified exec process') { 'RUNNER_BOOTSTRAP_BLOCKED' } else { 'OUTPUT_PACKAGE_MISSING' }
            $failureDetail = if ($failureCode -eq 'RUNNER_BOOTSTRAP_BLOCKED') {
                'O Codex CLI terminou sem ZIP e o runner recusou os helpers ou a escrita do workspace; verificar bootstrap/preflight do runner antes de retomar.'
            }
            else {
                'A execução terminou sem publicar um ZIP cujo nome identifique o último lote do ciclo.'
            }
            $State.status = 'BLOCKED'
            $State.last_error = [ordered]@{ code = $failureCode; detail = $failureDetail; at = Get-UtcTimestamp }
            $State.dispatches = @($State.dispatches | ForEach-Object { if ($_.idempotency_key -eq $key) { $_.status = 'FAILED' }; $_ })
            Save-CampaignState -State $State
            Add-HistoryEvent -Event 'CYCLE_FAILED' -Data $State.last_error
            return [pscustomobject]@{ success = $false; code = $failureCode; detail = $State.last_error.detail; cycle_id = $cycleId }
        }
        $validation = Test-ContinuityPackage -Path $outputPackage -ExpectedLastLot $Cycle.end -RequiredBaseLot ($Cycle.start - 1)
        if (-not $validation.pass) {
            $State.status = 'BLOCKED'
            $State.last_error = [ordered]@{ code = $validation.code; detail = $validation.detail; at = Get-UtcTimestamp }
            Set-ObjectProperty -Object $State.current_cycle -Name 'output_package' -Value $outputPackage
            Set-ObjectProperty -Object $State.current_cycle -Name 'output_package_sha256' -Value $validation.sha256
            Set-ObjectProperty -Object $State.current_cycle -Name 'audit' -Value $validation
            Save-CampaignState -State $State
            Add-HistoryEvent -Event 'AUDIT_FAILED' -Data ([ordered]@{ cycle_id = $cycleId; code = $validation.code; package = $outputPackage; sha256 = $validation.sha256 })
            return [pscustomobject]@{ success = $false; code = $validation.code; detail = $validation.detail; cycle_id = $cycleId; validation = $validation }
        }
        $next = Get-NextCycleFromValidation -Validation $validation
        $nextStart = if ($next) { [int]$next.start } else { $null }
        $nextEnd = if ($next) { [int]$next.end } else { $null }
        $transition = Apply-ValidatedCycleTransition -State $State -CycleStart $Cycle.start -CycleEnd $Cycle.end -PackageSha256 $ValidatedPackageSha256 -AuditPassed $true -CompleteFichas $validation.counts.complete_fichas -VerifiedImages $validation.counts.verified_images -TargetTotal 607 -NextStart $nextStart -NextEnd $nextEnd
        $State = $transition.state
        $State.package_base = [ordered]@{ path = $outputPackage; sha256 = $validation.sha256; last_lot = $Cycle.end; required_base_lot = $Cycle.start - 1 }
        Set-ObjectProperty -Object $State.current_cycle -Name 'output_package' -Value $outputPackage
        Set-ObjectProperty -Object $State.current_cycle -Name 'output_package_sha256' -Value $validation.sha256
        Set-ObjectProperty -Object $State.current_cycle -Name 'audit' -Value $validation
        Set-ObjectProperty -Object $State.current_cycle -Name 'result' -Value $transition.action
        if ($transition.action -eq 'READY_TO_DISPATCH') {
            $State.dispatches += [pscustomobject]([ordered]@{ idempotency_key = (Get-DispatchKey -StartLot $next.start -EndLot $next.end -PackageSha256 $validation.sha256); cycle = "$($next.start)-$($next.end)"; status = 'PENDING'; at = Get-UtcTimestamp })
        }
        Save-CampaignState -State $State
        Add-HistoryEvent -Event 'CHECKPOINT_VALIDATED' -Data ([ordered]@{ cycle_id = $cycleId; cycle = "$($Cycle.start)-$($Cycle.end)"; output_package = $outputPackage; output_sha256 = $validation.sha256; counts = $validation.counts; next_cycle = $State.next_cycle; transition = $transition.action })
        return [pscustomobject]@{ success = $true; code = $transition.action; detail = $validation.detail; cycle_id = $cycleId; validation = $validation; state = $State }
    }
    catch {
        $detail = Redact-Secrets $_.Exception.Message
        $State.status = 'BLOCKED'
        if ($null -ne $State.current_cycle) {
            $State.current_cycle.ended_at = Get-UtcTimestamp
            if ($process.HasExited) { $State.current_cycle.exit_code = $process.ExitCode }
        }
        $State.dispatches = @($State.dispatches | ForEach-Object {
            if ($_.idempotency_key -eq $key -and $_.status -eq 'STARTED') { $_.status = 'FAILED' }
            $_
        })
        $State.last_error = [ordered]@{ code = 'DISPATCH_EXCEPTION'; detail = $detail; at = Get-UtcTimestamp }
        Save-CampaignState -State $State
        Add-HistoryEvent -Event 'CYCLE_FAILED' -Data ([ordered]@{ cycle_id = $cycleId; error = $State.last_error; dispatch_status = 'FAILED' })
        return [pscustomobject]@{ success = $false; code = 'DISPATCH_EXCEPTION'; detail = $detail; cycle_id = $cycleId }
    }
    finally {
        $process.Dispose()
    }
}

function Invoke-RunCycles {
    param(
        [Parameter(Mandatory)]$State,
        [Parameter(Mandatory)][string]$TrustedWorkdir,
        [Parameter(Mandatory)]$CodexCapability,
        [int]$MaxCycles = 1000
    )
    for ($number = 0; $number -lt $MaxCycles; $number++) {
        $State = Read-CampaignState
        if ($State.status -in @('COMPLETED', 'BLOCKED', 'CANCELLED')) { return $State }
        if ($null -eq $State.next_cycle) {
            $State.status = 'BLOCKED'
            $State.last_error = [ordered]@{ code = 'NEXT_CYCLE_MISSING'; detail = 'Não há ciclo pendente para despacho.'; at = Get-UtcTimestamp }
            Save-CampaignState -State $State
            return $State
        }
        $basePath = [string]$State.package_base.path
        $baseSha = [string]$State.package_base.sha256
        $result = Invoke-CodexCycle -State $State -Cycle $State.next_cycle -ValidatedPackagePath $basePath -ValidatedPackageSha256 $baseSha -TrustedWorkdir $TrustedWorkdir -CodexCapability $CodexCapability
        if (-not $result.success -or $result.code -ne 'READY_TO_DISPATCH') { return (Read-CampaignState) }
    }
    $State = Read-CampaignState
    Set-BlockedState -State $State -Code 'MAX_CYCLES_REACHED' -Detail "O supervisor atingiu o limite de $MaxCycles ciclos sem concluir a campanha."
}

function Invoke-Run {
    $lockHandle = $null
    try {
        $lockHandle = New-LockHandle
        $state = Read-CampaignState
        if ($null -eq $state) { $state = New-CampaignState }
        if ($RetryFailed -and $state.status -eq 'BLOCKED' -and $null -ne $state.current_cycle) {
            $registeredPid = if ($state.current_cycle.pid) { [int]$state.current_cycle.pid } else { 0 }
            $live = if ($registeredPid) { Get-Process -Id $registeredPid -ErrorAction SilentlyContinue } else { $null }
            if ($null -eq $live) {
                $state.dispatches = @($state.dispatches | ForEach-Object {
                    if ($_.cycle -eq "$($state.current_cycle.start)-$($state.current_cycle.end)" -and $_.status -eq 'STARTED') { $_.status = 'FAILED' }
                    $_
                })
                $state.status = 'READY_TO_DISPATCH'
                $state.last_error = $null
                Save-CampaignState -State $state
                Add-HistoryEvent -Event 'FAILED_DISPATCH_RETRY_ARMED' -Data ([ordered]@{ cycle = "$($state.current_cycle.start)-$($state.current_cycle.end)"; previous_pid = $registeredPid })
            }
            else {
                [pscustomobject]@{ status = 'UNKNOWN'; code = 'RUNNING_PROCESS_STILL_ALIVE'; pid = $registeredPid; real_research_started = $false } | ConvertTo-Json
                return
            }
        }
        if ($state.status -eq 'COMPLETED') {
            [pscustomobject]@{ status = $state.status; code = 'ALREADY_COMPLETED'; real_research_started = $false } | ConvertTo-Json -Depth 10
            return
        }
        if (-not $PackagePath -and $state.package_base.path) { $PackagePath = [string]$state.package_base.path }
        if (-not $PackagePath) {
            $state = Set-BlockedState -State $state -Code 'PACKAGE_REQUIRED_FOR_RUN' -Detail 'Run exige o caminho do pacote LOTE20 validado.'
            [pscustomobject]@{ status = $state.status; code = 'PACKAGE_REQUIRED_FOR_RUN'; real_research_started = $false } | ConvertTo-Json -Depth 10
            return
        }
        $expectedLastLot = if ($state.package_base.last_lot -ne $null) { [int]$state.package_base.last_lot } else { $ExpectedLastLot }
        $requiredBaseProperty = $state.package_base.PSObject.Properties['required_base_lot']
        $requiredBaseLot = if ($null -ne $requiredBaseProperty -and $null -ne $requiredBaseProperty.Value) { [int]$requiredBaseProperty.Value } elseif ($expectedLastLot -gt 20) { $expectedLastLot - 5 } else { $RequiredBaseLot }
        $initialized = Initialize-FromPackage -Path ([IO.Path]::GetFullPath($PackagePath)) -State $state -ExpectedLastLot $expectedLastLot -RequiredBaseLot $requiredBaseLot
        $state = $initialized.state
        if (-not $initialized.validation.pass) {
            $state.status = 'BLOCKED'
            $state.last_error = [ordered]@{ code = $initialized.validation.code; detail = $initialized.validation.detail; at = Get-UtcTimestamp }
            Save-CampaignState -State $state
            Add-HistoryEvent -Event 'PACKAGE_REJECTED' -Data ([ordered]@{ code = $initialized.validation.code; sha256 = $initialized.validation.sha256 })
            [pscustomobject]@{ status = $state.status; code = $initialized.validation.code; detail = $initialized.validation.detail; real_research_started = $false } | ConvertTo-Json -Depth 20
            return
        }
        if (-not $Workdir) {
            $state = Set-BlockedState -State $state -Code 'WORKDIR_REQUIRED' -Detail 'Run exige um repositório Git explícito para a execução local.'
            [pscustomobject]@{ status = $state.status; code = 'WORKDIR_REQUIRED'; real_research_started = $false } | ConvertTo-Json -Depth 10
            return
        }
        $trusted = Test-TrustedGitWorkdir -Path ([IO.Path]::GetFullPath($Workdir))
        $capability = Test-CodexCapabilities
        $state.workdir = $trusted
        $state.status = 'READY_TO_DISPATCH'
        $state.codex = $capability
        $state.last_error = $null
        Save-CampaignState -State $state
        Add-HistoryEvent -Event 'PREFLIGHT_PASSED' -Data $capability
        $final = Invoke-RunCycles -State $state -TrustedWorkdir $trusted -CodexCapability $capability
        [pscustomobject]@{ status = $final.status; code = if($final.last_error){$final.last_error.code}else{$final.status}; state_path = $script:StatePath; current_cycle = $final.current_cycle; next_cycle = $final.next_cycle; real_research_started = $true } | ConvertTo-Json -Depth 20
    }
    catch {
        $state = Read-CampaignState
        if ($null -eq $state) { $state = New-CampaignState }
        $detail = Redact-Secrets $_.Exception.Message
        $code = if ($detail -match '^WORKDIR_NOT_TRUSTED') { 'WORKDIR_NOT_TRUSTED' } elseif ($detail -match '^CODEX_') { ($detail -split ':')[0] } elseif ($detail -match 'CAMPAIGN_LOCK_HELD') { 'CAMPAIGN_LOCK_HELD' } else { 'RUN_PREFLIGHT_FAILED' }
        if ($code -ne 'CAMPAIGN_LOCK_HELD') { Set-BlockedState -State $state -Code $code -Detail $detail | Out-Null }
        [pscustomobject]@{ status = if($code -eq 'CAMPAIGN_LOCK_HELD'){'LOCKED'}else{'BLOCKED'}; code = $code; detail = $detail; state_path = $script:StatePath; real_research_started = $false } | ConvertTo-Json -Depth 10
    }
    finally {
        Release-LockHandle -Handle $lockHandle
    }
}

function Invoke-Resume {
    $state = Read-CampaignState
    if ($null -eq $state) {
        [pscustomobject]@{ status = 'BLOCKED'; code = 'NO_DURABLE_STATE'; real_research_started = $false } | ConvertTo-Json
        return
    }
    if ($state.status -in @('COMPLETED', 'CANCELLED', 'BLOCKED')) {
        [pscustomobject]@{ status = $state.status; code = 'TERMINAL_NOOP'; last_error = $state.last_error; real_research_started = $false } | ConvertTo-Json -Depth 12
        return
    }
    if ($state.status -eq 'RUNNING' -and $state.current_cycle.pid) {
        $live = Get-Process -Id ([int]$state.current_cycle.pid) -ErrorAction SilentlyContinue
        if ($null -ne $live) {
            [pscustomobject]@{ status = 'UNKNOWN'; code = 'RUNNING_PROCESS_STILL_ALIVE'; pid = $state.current_cycle.pid; real_research_started = $false } | ConvertTo-Json
            return
        }
        $state.status = 'UNKNOWN'
        $state.last_error = [ordered]@{ code = 'PROCESS_EXITED_BEFORE_RESUME_CONFIRMATION'; detail = 'O processo registrado não está vivo; o supervisor não o repete automaticamente.'; at = Get-UtcTimestamp }
        Save-CampaignState -State $state
        Add-HistoryEvent -Event 'RESUME_UNKNOWN' -Data $state.last_error
        [pscustomobject]@{ status = $state.status; code = $state.last_error.code; real_research_started = $false } | ConvertTo-Json -Depth 10
        return
    }
    if ($state.status -eq 'UNKNOWN') {
        [pscustomobject]@{ status = $state.status; code = 'MANUAL_RECONCILIATION_REQUIRED'; detail = 'Reconcilie o processo e o pacote publicado antes de retomar; nenhum lote foi repetido.'; real_research_started = $false } | ConvertTo-Json
        return
    }
    if (-not $Workdir) { $Workdir = [string]$state.workdir }
    if (-not $PackagePath) { $PackagePath = [string]$state.package_base.path }
    Invoke-Run
}

function Invoke-Reconcile {
    $lockHandle = $null
    try {
        $lockHandle = New-LockHandle
        $state = Read-CampaignState
        if ($null -eq $state -or $null -eq $state.current_cycle) {
            [pscustomobject]@{ status = 'BLOCKED'; code = 'NO_CYCLE_TO_RECONCILE'; real_research_started = $false } | ConvertTo-Json
            return
        }
        $registeredPid = if ($state.current_cycle.pid) { [int]$state.current_cycle.pid } else { 0 }
        if ($registeredPid -and (Get-Process -Id $registeredPid -ErrorAction SilentlyContinue)) {
            [pscustomobject]@{ status = 'UNKNOWN'; code = 'RUNNING_PROCESS_STILL_ALIVE'; pid = $registeredPid; real_research_started = $false } | ConvertTo-Json
            return
        }
        $cycleEnd = [int]$state.current_cycle.end
        $cycleStart = [int]$state.current_cycle.start
        $startedValue = $state.current_cycle.started_at
        $startedAt = if ($startedValue -is [datetime]) {
            $startedValue.ToUniversalTime()
        }
        else {
            [datetime]::Parse([string]$startedValue, [Globalization.CultureInfo]::InvariantCulture, [Globalization.DateTimeStyles]::AssumeUniversal -bor [Globalization.DateTimeStyles]::AdjustToUniversal)
        }
        $candidate = Find-CyclePackage -OutputDirectory ([string]$state.current_cycle.output_directory) -EndLot $cycleEnd -StartedAt $startedAt
        $recoverableFailure = $state.status -eq 'BLOCKED' -and $state.last_error -and ([string]$state.last_error.code -in @('DISPATCH_EXCEPTION', 'OUTPUT_PACKAGE_MISSING', 'RUNNER_BOOTSTRAP_BLOCKED'))
        if ($candidate -and ($state.status -ne 'BLOCKED' -or $recoverableFailure)) {
            $validation = Test-ContinuityPackage -Path $candidate -ExpectedLastLot $cycleEnd -RequiredBaseLot ($cycleStart - 1)
            if ($validation.pass) {
                if ($state.status -eq 'BLOCKED') {
                    $state.status = 'READY_TO_DISPATCH'
                    $state.last_error = $null
                }
                $next = Get-NextCycleFromValidation -Validation $validation
                $nextStart = if ($next) { [int]$next.start } else { $null }
                $nextEnd = if ($next) { [int]$next.end } else { $null }
                $inputBaseSha = if ($state.current_cycle.package_base_sha256) { [string]$state.current_cycle.package_base_sha256 } else { [string]$state.package_base.sha256 }
                $transition = Apply-ValidatedCycleTransition -State $state -CycleStart $cycleStart -CycleEnd $cycleEnd -PackageSha256 $inputBaseSha -AuditPassed $true -CompleteFichas $validation.counts.complete_fichas -VerifiedImages $validation.counts.verified_images -TargetTotal 607 -NextStart $nextStart -NextEnd $nextEnd
                $state = $transition.state
                $state.package_base = [ordered]@{ path = $candidate; sha256 = $validation.sha256; last_lot = $cycleEnd; required_base_lot = $cycleStart - 1 }
                Set-ObjectProperty -Object $state.current_cycle -Name 'output_package' -Value $candidate
                Set-ObjectProperty -Object $state.current_cycle -Name 'output_package_sha256' -Value $validation.sha256
                Set-ObjectProperty -Object $state.current_cycle -Name 'audit' -Value $validation
                Set-ObjectProperty -Object $state.current_cycle -Name 'result' -Value $transition.action
                if ($transition.action -eq 'READY_TO_DISPATCH') {
                    Register-DispatchIfNeeded -State $state -CycleStart $nextStart -CycleEnd $nextEnd -PackageSha256 $validation.sha256 | Out-Null
                }
                Save-CampaignState -State $state
                Add-HistoryEvent -Event 'CHECKPOINT_RECONCILED' -Data ([ordered]@{ cycle_id = $state.current_cycle.cycle_id; package = $candidate; sha256 = $validation.sha256; counts = $validation.counts; transition = $transition.action })
                [pscustomobject]@{ status = $state.status; code = $transition.action; package = $candidate; package_sha256 = $validation.sha256; next_cycle = $state.next_cycle; real_research_started = $false } | ConvertTo-Json -Depth 12
                return
            }
            $state.status = 'BLOCKED'
            $state.last_error = [ordered]@{ code = $validation.code; detail = $validation.detail; at = Get-UtcTimestamp }
            Set-ObjectProperty -Object $state.current_cycle -Name 'output_package' -Value $candidate
            Set-ObjectProperty -Object $state.current_cycle -Name 'output_package_sha256' -Value $validation.sha256
            Set-ObjectProperty -Object $state.current_cycle -Name 'audit' -Value $validation
            $state.dispatches = @($state.dispatches | ForEach-Object { if ($_.cycle -eq "$cycleStart-$cycleEnd" -and $_.status -in @('STARTED', 'PENDING')) { $_.status = 'FAILED' }; $_ })
            Save-CampaignState -State $state
            Add-HistoryEvent -Event 'AUDIT_FAILED_RECONCILE' -Data ([ordered]@{ cycle_id = $state.current_cycle.cycle_id; code = $validation.code; package = $candidate; sha256 = $validation.sha256 })
            [pscustomobject]@{ status = $state.status; code = $validation.code; package = $candidate; real_research_started = $false } | ConvertTo-Json -Depth 12
            return
        }
        $stderr = if ($state.current_cycle.stderr_path -and (Test-Path -LiteralPath $state.current_cycle.stderr_path)) { Get-Content -Raw -LiteralPath $state.current_cycle.stderr_path } else { '' }
        $all = Redact-Secrets $stderr
        $lastErrorCode = if ($state.last_error -and $state.last_error.code) { [string]$state.last_error.code } else { '' }
        $code = if ($all -match '(?i)helper_unknown_error|setup refresh had errors|failed to write file|failed to create unified exec process') { 'RUNNER_BOOTSTRAP_BLOCKED' } elseif ($lastErrorCode) { $lastErrorCode } else { 'MANUAL_RECONCILIATION_REQUIRED' }
        $detail = if ($code -eq 'RUNNER_BOOTSTRAP_BLOCKED') { 'O runner recusou helpers ou a escrita do workspace; corrigir bootstrap/preflight antes de retomar.' } else { 'Falha do ciclo reconciliada sem evidência de pacote válido; verificar os artefatos antes de retomar.' }
        $state.status = 'BLOCKED'
        $state.last_error = [ordered]@{ code = $code; detail = $detail; at = Get-UtcTimestamp }
        $state.dispatches = @($state.dispatches | ForEach-Object { if ($_.cycle -eq "$($state.current_cycle.start)-$($state.current_cycle.end)" -and $_.status -eq 'STARTED') { $_.status = 'FAILED' }; $_ })
        Save-CampaignState -State $state
        Add-HistoryEvent -Event 'FAILURE_RECONCILED' -Data $state.last_error
        [pscustomobject]@{ status = $state.status; code = $code; state_path = $script:StatePath; real_research_started = $false } | ConvertTo-Json -Depth 10
    }
    finally {
        Release-LockHandle -Handle $lockHandle
    }
}

function Invoke-Cancel {
    $lockHandle = $null
    try {
        $lockHandle = New-LockHandle
        $state = Read-CampaignState
        if ($null -eq $state) {
            [pscustomobject]@{ status = 'BLOCKED'; code = 'NO_DURABLE_STATE' } | ConvertTo-Json
            return
        }
        if ($state.current_cycle.pid) {
            $process = Get-Process -Id ([int]$state.current_cycle.pid) -ErrorAction SilentlyContinue
            if ($null -ne $process) {
                Stop-Process -Id $process.Id -Force
                $state.current_cycle.cancelled_at = Get-UtcTimestamp
            }
        }
        $state.status = 'CANCELLED'
        $state.last_error = [ordered]@{ code = 'CANCELLED_BY_OPERATOR'; detail = 'Campanha cancelada explicitamente; não haverá próximo despacho.'; at = Get-UtcTimestamp }
        Save-CampaignState -State $state
        Add-HistoryEvent -Event 'CANCELLED' -Data $state.last_error
        [pscustomobject]@{ status = $state.status; code = 'CANCELLED_BY_OPERATOR'; real_research_started = $false } | ConvertTo-Json
    }
    finally { Release-LockHandle -Handle $lockHandle }
}

switch ($Mode) {
    'SelfTest' { Invoke-SelfTest; break }
    'Simulate' { Invoke-Simulation; break }
    'Prepare' { Invoke-Prepare; break }
    'Run' { Invoke-Run; break }
    'Resume' { Invoke-Resume; break }
    'Reconcile' { Invoke-Reconcile; break }
    'Cancel' { Invoke-Cancel; break }
}
