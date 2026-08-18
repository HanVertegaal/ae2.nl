$ErrorActionPreference = "Stop"

$RepoPath = "C:\Users\han\Documents\Projects\ae2.nl"
$DocsPath = Join-Path $RepoPath "docs"

Set-Location $RepoPath

if (-not (Test-Path $DocsPath)) {
    throw "Docs folder not found at: $DocsPath"
}

Write-Host "Starting local static preview server..."
Write-Host "Open: http://127.0.0.1:8000/"
Write-Host "Press Ctrl+C to stop."
Write-Host ""

python -m http.server 8000 --directory $DocsPath