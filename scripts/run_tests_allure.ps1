# Запуск тестов с записью Allure-результатов
param(
    [string]$Markers = "",
    [string]$ResultsDir = "reports/allure-results",
    [string]$ExtraArgs = ""
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $PSScriptRoot
Set-Location $ProjectRoot

$venvPytest = Join-Path $ProjectRoot ".venv\Scripts\pytest.exe"
if (-not (Test-Path $venvPytest)) {
    $venvPytest = "pytest"
}

$env:ALLURE_RESULTS_DIR = $ResultsDir

$pytestArgs = @(
    "tests",
    "--alluredir=$ResultsDir",
    "--clean-alluredir",
    "--browser", "chromium",
    "-v"
)

if ($Markers) {
    $pytestArgs += @("-m", $Markers)
}

if ($ExtraArgs) {
    $pytestArgs += $ExtraArgs.Split(" ")
}

Write-Host ">> pytest $($pytestArgs -join ' ')" -ForegroundColor Cyan
& $venvPytest @pytestArgs
$exitCode = $LASTEXITCODE

Write-Host ""
Write-Host "Allure results: $ResultsDir" -ForegroundColor Green
Write-Host "Generate report: .\scripts\allure_report.ps1" -ForegroundColor Green

exit $exitCode
