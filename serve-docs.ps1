$ErrorActionPreference = "Stop"

$RepoPath = "C:\Users\han\Documents\Projects\ae2.nl"
$VenvActivate = Join-Path $RepoPath ".venv\Scripts\Activate.ps1"

Set-Location $RepoPath

if (-not (Test-Path $VenvActivate)) {
    Write-Host "Creating Python virtual environment..."
    python -m venv .venv
}

Write-Host "Activating virtual environment..."
& $VenvActivate

Write-Host "Installing/updating MkDocs dependencies..."
python -m pip install --upgrade pip
python -m pip install mkdocs mkdocs-material pymdown-extensions

Write-Host ""
Write-Host "Starting MkDocs preview server..."
Write-Host "Open: http://127.0.0.1:8000"
Write-Host "Press Ctrl+C to stop."
Write-Host ""

mkdocs serve