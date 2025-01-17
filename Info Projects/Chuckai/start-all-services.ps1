# Start-All-Services.ps1
# Script to start both Ollama and Stable Diffusion services

Write-Host "Starting All AI Services..." -ForegroundColor Green

# Function to download file with progress bar
function Download-File {
    param(
        [string]$Url,
        [string]$OutputPath
    )
    $webClient = New-Object System.Net.WebClient
    $webClient.DownloadFile($Url, $OutputPath)
}

# First, start Ollama and Open WebUI
Write-Host "Starting Ollama and Open WebUI..." -ForegroundColor Yellow
& .\start-ai-environment.ps1

# Verify Stable Diffusion model exists
$modelPath = "stable-diffusion/stable-diffusion-webui/models/Stable-diffusion/v1-5-pruned-emaonly.safetensors"
if (-not (Test-Path $modelPath)) {
    Write-Host "Error: Stable Diffusion model not found. Please run .\download-sd-model.ps1 first." -ForegroundColor Red
    exit 1
}

# Start Stable Diffusion Web UI
Write-Host "Starting Stable Diffusion Web UI..." -ForegroundColor Yellow
$sdProcess = Start-Process -FilePath "cmd.exe" -ArgumentList "/c cd stable-diffusion\stable-diffusion-webui && webui.bat" -PassThru -WindowStyle Normal

Write-Host "`nAll services are starting!" -ForegroundColor Green
Write-Host "Available interfaces:" -ForegroundColor Cyan
Write-Host "- Ollama Web UI: http://localhost:8080" -ForegroundColor Cyan
Write-Host "- Stable Diffusion: http://localhost:7860" -ForegroundColor Cyan

Write-Host "`nAvailable commands:" -ForegroundColor Cyan
Write-Host "- '.\stop-ai-environment.ps1' to stop Ollama services" -ForegroundColor Cyan
Write-Host "- Use Ctrl+C in the Stable Diffusion window to stop it" -ForegroundColor Cyan

# Open web interfaces
Start-Process "http://localhost:8080"
Start-Sleep -Seconds 5  # Wait a bit before opening the second interface
Start-Process "http://localhost:7860"
