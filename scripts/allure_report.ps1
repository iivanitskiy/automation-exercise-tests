# Генерация и открытие HTML-отчёта Allure
param(
    [string]$ResultsDir = "reports/allure-results",
    [string]$ReportDir = "reports/allure-report",
    [switch]$Serve,
    [switch]$OpenOnly
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $PSScriptRoot
Set-Location $ProjectRoot
$ConfigDir = Join-Path $ProjectRoot "config\allure"

function Find-Allure {
    $cmd = Get-Command allure -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }

    $candidates = @(
        "$env:USERPROFILE\scoop\shims\allure.cmd",
        "$env:ProgramFiles\allure\bin\allure.bat",
        "$env:LOCALAPPDATA\Microsoft\WinGet\Links\allure.exe"
    )
    foreach ($path in $candidates) {
        if (Test-Path $path) { return $path }
    }
    return $null
}

$allure = Find-Allure
if (-not $allure) {
    Write-Host "Allure CLI не найден. Установите одним из способов:" -ForegroundColor Yellow
    Write-Host "  scoop install allure"
    Write-Host "  choco install allure-commandline"
    Write-Host "  npm install -g allure-commandline --save-dev"
    Write-Host ""
    Write-Host "Или скачайте: https://github.com/allure-framework/allure2/releases" -ForegroundColor Yellow
    exit 1
}

if (-not $OpenOnly) {
    if (-not (Test-Path $ResultsDir)) {
        Write-Host "Нет результатов: $ResultsDir. Сначала запустите .\scripts\run_tests_allure.ps1" -ForegroundColor Red
        exit 1
    }

    $generateArgs = @(
        "generate", $ResultsDir,
        "-o", $ReportDir,
        "--clean",
        "--config", $ConfigDir
    )
    Write-Host ">> allure $($generateArgs -join ' ')" -ForegroundColor Cyan
    & $allure @generateArgs
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}

if ($Serve) {
    Write-Host ">> allure open $ReportDir" -ForegroundColor Cyan
    & $allure open $ReportDir
} else {
    $indexPath = Join-Path $ReportDir "index.html"
    if (Test-Path $indexPath) {
        Write-Host "Report: $indexPath" -ForegroundColor Green
        Start-Process $indexPath
    }
}
