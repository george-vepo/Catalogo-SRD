#requires -Version 7.0

[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$scriptPath = Join-Path $PSScriptRoot '..\Start-SRDCampaignSupervisor.ps1'
$jsonText = & pwsh -NoProfile -File $scriptPath -Mode SelfTest
if ($LASTEXITCODE -ne 0) {
    throw "Supervisor self-test failed with exit code $LASTEXITCODE"
}
$result = ($jsonText | Out-String | ConvertFrom-Json)
if ($result.result -ne 'PASS') { throw "Unexpected self-test result: $($result.result)" }
if ([int]$result.test_count -lt 11) { throw "Expected at least 11 behavioral tests, got $($result.test_count)" }
if ($result.codex_invoked -ne $false) { throw 'Self-test must not invoke Codex CLI' }
if ($result.real_research_started -ne $false) { throw 'Self-test must not start real research' }

[pscustomobject]@{
    test = 'Test-SRDCampaignSupervisor'
    result = 'PASS'
    delegated_tests = $result.test_count
    evidence_path = $result.evidence_path
} | ConvertTo-Json -Depth 10
