#requires -Version 7.0

[CmdletBinding()]
param(
    [Parameter(Mandatory)][string]$OutputRoot,
    [Parameter(Mandatory)][string]$SourceRoot,
    [Parameter(Mandatory)][string]$PackagePath,
    [Parameter(Mandatory)][int]$CycleStart,
    [Parameter(Mandatory)][int]$CycleEnd,
    [Parameter(Mandatory)][int]$NextStart,
    [Parameter(Mandatory)][int]$NextEnd,
    [Parameter(Mandatory)][int]$CompleteFichas,
    [Parameter(Mandatory)][int]$VerifiedImages,
    [string]$PreviousPackagePath,
    [string]$PackageBaseDescription = 'Inventário-base local; não tratado como pacote LOTE20.'
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Write-Utf8NoBom {
    param([Parameter(Mandatory)][string]$Path, [Parameter(Mandatory)][string]$Text)
    $parent = Split-Path -Parent $Path
    if (-not (Test-Path -LiteralPath $parent -PathType Container)) {
        New-Item -ItemType Directory -Path $parent -Force | Out-Null
    }
    [IO.File]::WriteAllText($Path, $Text, [Text.UTF8Encoding]::new($false))
}

function Copy-RequiredFile {
    param([Parameter(Mandatory)][string]$From, [Parameter(Mandatory)][string]$To)
    if (-not (Test-Path -LiteralPath $From -PathType Leaf)) {
        throw "REQUIRED_FILE_MISSING:$From"
    }
    $parent = Split-Path -Parent $To
    if (-not (Test-Path -LiteralPath $parent -PathType Container)) {
        New-Item -ItemType Directory -Path $parent -Force | Out-Null
    }
    Copy-Item -LiteralPath $From -Destination $To -Force
}

$sourceRoot = [IO.Path]::GetFullPath($SourceRoot)
$outputRoot = [IO.Path]::GetFullPath($OutputRoot)
$packagePath = [IO.Path]::GetFullPath($PackagePath)
if (Test-Path -LiteralPath $packagePath) {
    throw "PACKAGE_EXISTS_REFUSING_OVERWRITE:$packagePath"
}
if ($CycleEnd - $CycleStart -ne 4 -or $NextEnd - $NextStart -ne 4 -or $NextStart -ne $CycleEnd + 1) {
    throw 'CYCLE_RANGE_INVALID:each cycle must contain five contiguous positions'
}
if ($CompleteFichas -lt 0 -or $CompleteFichas -gt 607 -or $VerifiedImages -lt 0 -or $VerifiedImages -gt 607) {
    throw 'COUNTS_OUT_OF_RANGE'
}
if ($PreviousPackagePath -and -not (Test-Path -LiteralPath $PreviousPackagePath -PathType Leaf)) {
    throw "PREVIOUS_PACKAGE_MISSING:$PreviousPackagePath"
}

$version = '2.1.0'
$artifactRootName = '02_SAIDA_v2.1.0'
$stage = Join-Path ([IO.Path]::GetTempPath()) ("srd-continuity-cycle-{0}-{1}" -f $CycleStart, ([guid]::NewGuid().ToString('N')))
New-Item -ItemType Directory -Path $stage -Force | Out-Null
try {
    $artifactRoot = Join-Path $stage $artifactRootName
    $constructorRoot = Join-Path $stage '03_CONSTRUTOR'
    $inputsRoot = Join-Path $stage '04_INSUMOS'
    New-Item -ItemType Directory -Path (Join-Path $stage '01_CONTINUIDADE') -Force | Out-Null
    New-Item -ItemType Directory -Path $artifactRoot -Force | Out-Null
    New-Item -ItemType Directory -Path $constructorRoot -Force | Out-Null
    New-Item -ItemType Directory -Path $inputsRoot -Force | Out-Null
    if ($PreviousPackagePath) {
        New-Item -ItemType Directory -Path (Join-Path $stage '00_PACOTE_BASE') -Force | Out-Null
        $previousName = Split-Path -Leaf $PreviousPackagePath
        Copy-RequiredFile -From ([IO.Path]::GetFullPath($PreviousPackagePath)) -To (Join-Path (Join-Path $stage '00_PACOTE_BASE') $previousName)
    }

    $embeddedZipCandidates = @(Get-ChildItem -LiteralPath $outputRoot -Filter 'SRD_FICHAS_IMAGENS_607_v*.zip' -File)
    if ($embeddedZipCandidates.Count -ne 1) {
        throw "EMBEDDED_IMAGE_ZIP_EXPECTED_EXACTLY_ONE:$outputRoot"
    }
    $embeddedZipName = $embeddedZipCandidates[0].Name

    $outputFiles = @(
        'SRD_FICHAS_607_COMPLETAS.docx',
        'SRD_FICHAS_607.json',
        'SRD_URLS_IMAGENS_607.docx',
        'SRD_URLS_IMAGENS_607.csv',
        'SRD_AUDITORIA_PENDENCIAS_607.csv',
        'SRD_RELATORIO_DE_COLETA.md',
        'SRD_Card_Game_Fichas_607_Fontes_Web_Lote1.csv',
        $embeddedZipName
    )
    foreach ($name in $outputFiles) {
        Copy-RequiredFile -From (Join-Path $outputRoot $name) -To (Join-Path $artifactRoot $name)
    }

    $constructorFiles = @(
        'LEIA-ME.txt',
        'build_deliverables.py',
        'SRD_Card_Game_Fichas_607_Indice_e_Textos_Extraidos.json',
        'SRD_Worker_Base_Pendencias_607.csv',
        'SRD_Card_Game_Fichas_607_Fontes_Web_Lote2.csv',
        'SRD_Card_Game_Referencia_URL_Imagens_607_v3.csv'
    )
    foreach ($name in $constructorFiles) {
        Copy-RequiredFile -From (Join-Path (Join-Path $sourceRoot '03_CONSTRUTOR') $name) -To (Join-Path $constructorRoot $name)
    }
    foreach ($name in @('SRD_Worker_Prompt_Completo_Fichas_Imagens_607.txt','SRD_Worker_Manifesto_607.json')) {
        Copy-RequiredFile -From (Join-Path (Join-Path $sourceRoot '04_INSUMOS') $name) -To (Join-Path $inputsRoot $name)
    }

    $packageName = Split-Path -Leaf $packagePath
    $stateText = @"
# SRD Card Game 607 — estado de continuidade

## Checkpoint LOTE$CycleEnd (ciclo operacional $CycleStart–$CycleEnd)

- Este é o checkpoint do ciclo operacional $CycleStart–$CycleEnd; cada ciclo contém exatamente cinco posições e não depende da numeração histórica dos lotes.
- O ciclo concluiu $CompleteFichas/607 fichas mecânicas completas e $VerifiedImages/607 imagens diretas verificadas segundo os artefatos deste pacote.
- JSON, auditoria CSV, imagens CSV e índice de fontes preservam 607 IDs únicos; nenhum ID foi criado ou removido.
- O pacote mantém a exclusão declarada de 28 homebrews autorais próprios; homebrews publicados por Kobold Press, EN Publishing/A5E e MCDM continuam elegíveis quando válidos.
- $PackageBaseDescription
- O pacote de continuidade deste checkpoint é $packageName.

## Próximo ciclo

- Próximo ciclo operacional: lotes $NextStart a $NextEnd.
- A nova execução deve selecionar exatamente as cinco próximas fichas pendentes a partir do estado confirmado, sem repetir IDs já completos.
- Só avance depois de validar todos os artefatos, hashes, contagens, documentos e ZIPs.
- Se houver falha, preflight, credential broker, auditoria ou empacotamento inválido, preserve este checkpoint e marque o ciclo como BLOQUEADO/FALHOU.
"@
    Write-Utf8NoBom -Path (Join-Path $stage '01_CONTINUIDADE/ESTADO_ATUAL.md') -Text $stateText

    $promptText = @"
Você é a próxima execução independente do Codex CLI local para a campanha SRD Card Game 607.

Não use `codex exec resume`, não crie nem simule conversa do ChatGPT e não use automação de navegador para abrir conversas. Esta é uma execução nova e isolada.

Pacote de continuidade-base: $packagePath
Intervalo operacional: lotes $NextStart a $NextEnd (exatamente cinco posições consecutivas: $NextStart, $($NextStart + 1), $($NextStart + 2), $($NextStart + 3) e $NextEnd).
Contagens confirmadas no checkpoint: fichas completas=$CompleteFichas/607; imagens diretas verificadas=$VerifiedImages/607.

Selecione as cinco próximas fichas pendentes do JSON, mantendo exatamente os 607 IDs. Pesquise as mecânicas e as imagens apenas com fatos verificáveis; preserve pendências quando a fonte não permitir confirmação. Gere e audite DOCX, JSON, CSVs, relatório, manifesto SHA-256 e ZIP. O resultado deve ser um novo pacote de continuidade em um diretório de ciclo seguinte, sem sobrescrever este pacote, com 00_PACOTE_BASE apontando para ele e com o próximo intervalo de cinco posições no prompt.

Não grave credenciais, tokens ou segredos. Não invente status HTTP, imagens, estatísticas, IDs ou limites. Se o runner, preflight, credential broker ou qualquer validador bloquear, deixe o bloqueio explícito e termine com falha; não transforme bloqueio em sucesso.
"@
    Write-Utf8NoBom -Path (Join-Path $stage '01_CONTINUIDADE/PROMPT_PROXIMO_PROCESSO.txt') -Text $promptText

    $manifestEntries = [Collections.Generic.List[object]]::new()
    foreach ($file in (Get-ChildItem -LiteralPath $stage -Recurse -File | Where-Object { $_.FullName -ne (Join-Path $stage '01_CONTINUIDADE/MANIFESTO_SHA256.json') })) {
        $relative = $file.FullName.Substring($stage.Length + 1).Replace('\','/')
        $manifestEntries.Add([ordered]@{
            arquivo = $relative
            tamanho_bytes = $file.Length
            sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $file.FullName).Hash.ToLowerInvariant()
        })
    }
    $manifest = [ordered]@{
        schema_version = '1.0.0'
        pacote = $packageName
        campanha = 'SRD-607'
        ciclo = "$CycleStart-$CycleEnd"
        proximo_ciclo = "$NextStart-$NextEnd"
        total_ids = 607
        fichas_completas = $CompleteFichas
        imagens_diretas_verificadas = $VerifiedImages
        arquivos = @($manifestEntries)
    }
    Write-Utf8NoBom -Path (Join-Path $stage '01_CONTINUIDADE/MANIFESTO_SHA256.json') -Text ($manifest | ConvertTo-Json -Depth 20)

    $packageParent = Split-Path -Parent $packagePath
    if (-not (Test-Path -LiteralPath $packageParent -PathType Container)) {
        New-Item -ItemType Directory -Path $packageParent -Force | Out-Null
    }
    Add-Type -AssemblyName System.IO.Compression.FileSystem
    [IO.Compression.ZipFile]::CreateFromDirectory($stage, $packagePath, [IO.Compression.CompressionLevel]::Optimal, $false)
    $zip = [IO.Compression.ZipFile]::OpenRead($packagePath)
    try { foreach ($entry in $zip.Entries) { if (-not $entry.FullName.EndsWith('/')) { $null = $entry.Length } } }
    finally { $zip.Dispose() }
    [ordered]@{
        package = $packagePath
        sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $packagePath).Hash.ToLowerInvariant()
        cycle = "$CycleStart-$CycleEnd"
        next_cycle = "$NextStart-$NextEnd"
        complete_fichas = $CompleteFichas
        verified_images = $VerifiedImages
        staging_directory = $stage
    } | ConvertTo-Json -Depth 10
}
catch {
    throw
}
