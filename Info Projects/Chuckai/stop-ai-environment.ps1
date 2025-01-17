# Stop-AI-Environment.ps1
# Script to safely stop Ollama and Open WebUI

Write-Host "Stopping AI Environment..." -ForegroundColor Yellow

# Stop Docker container
Write-Host "Stopping Open WebUI container..." -ForegroundColor Yellow
docker stop open-webui 2>$null
if ($LASTEXITCODE -eq 0) {
    Write-Host "Open WebUI container stopped successfully" -ForegroundColor Green
} else {
    Write-Host "No Open WebUI container was running" -ForegroundColor Cyan
}

# Stop Ollama process in WSL
Write-Host "Stopping Ollama process in WSL..." -ForegroundColor Yellow
$wsl_check = wsl -d Ubuntu -- pgrep ollama
if ($wsl_check) {
    wsl -d Ubuntu -- sudo killall ollama
    Write-Host "Ollama process stopped successfully in WSL" -ForegroundColor Green
} else {
    Write-Host "No Ollama process was running in WSL" -ForegroundColor Cyan
}

Write-Host "`nAI Environment has been stopped!" -ForegroundColor Green
Write-Host "To start the environment again, run: .\start-ai-environment.ps1" -ForegroundColor Cyan
