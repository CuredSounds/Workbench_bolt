# Start-AI-Environment.ps1
# Script to automate Ollama and Open WebUI startup

Write-Host "Starting AI Environment..." -ForegroundColor Green

# Function to check if a process is running
function Test-ProcessRunning {
    param($ProcessName)
    return Get-Process $ProcessName -ErrorAction SilentlyContinue
}

# Function to check if Docker container is running
function Test-DockerContainer {
    param($ContainerName)
    $container = docker ps -q -f name=$ContainerName
    return $container -ne $null
}

# Check and start Ollama
Write-Host "Checking Ollama status..." -ForegroundColor Yellow
$ollamaProcess = Get-Process "ollama" -ErrorAction SilentlyContinue
if (-not $ollamaProcess) {
    Write-Host "Starting Ollama..." -ForegroundColor Yellow
    Start-Process "ollama" -ArgumentList "serve" -WindowStyle Hidden
    Start-Sleep -Seconds 10
} else {
    Write-Host "Ollama is already running" -ForegroundColor Green
}

# Verify Ollama models
Write-Host "Verifying Ollama models..." -ForegroundColor Yellow
$models = ollama list
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error checking Ollama models. Please ensure Ollama is installed correctly." -ForegroundColor Red
    exit 1
}
Write-Host "Available models:" -ForegroundColor Green
$models | ForEach-Object { Write-Host $_ }

# Check Docker container
Write-Host "Checking Open WebUI container..." -ForegroundColor Yellow
if (-not (Test-DockerContainer "open-webui")) {
    Write-Host "Starting Open WebUI container..." -ForegroundColor Yellow
    
    # Remove existing container if it exists but not running
    docker rm -f open-webui 2>$null
    
    # Start new container
    docker run -d --name open-webui `
        -p 8080:8080 `
        -v open-webui:/app/backend/data `
        -e OLLAMA_BASE_URL=http://host.docker.internal:11434 `
        --restart unless-stopped `
        ghcr.io/open-webui/open-webui:main
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Error starting Open WebUI container" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "Open WebUI container is already running" -ForegroundColor Green
}

# Wait for services to be ready
Write-Host "Waiting for services to be ready..." -ForegroundColor Yellow
Start-Sleep -Seconds 10

# Check if web interface is accessible
Write-Host "Checking web interface..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8080" -Method Head
    if ($response.StatusCode -eq 200) {
        Write-Host "Web interface is accessible" -ForegroundColor Green
    }
} catch {
    Write-Host "Warning: Web interface may not be ready yet. Please wait a few more seconds." -ForegroundColor Yellow
}

# Final instructions
Write-Host "`nAI Environment Setup Complete!" -ForegroundColor Green
Write-Host "You can access the web interface at: http://localhost:8080" -ForegroundColor Cyan
Write-Host "Available commands:" -ForegroundColor Cyan
Write-Host "- 'ollama list' to see available models" -ForegroundColor Cyan
Write-Host "- 'ollama pull llama2' to download new models" -ForegroundColor Cyan
Write-Host "- 'docker logs open-webui' to check container logs" -ForegroundColor Cyan
Write-Host "- 'docker restart open-webui' to restart the web interface" -ForegroundColor Cyan
Write-Host "- '.\stop-ai-environment.ps1' to stop all services" -ForegroundColor Cyan

# Open web browser
Write-Host "`nOpening web interface in default browser..." -ForegroundColor Yellow
Start-Process "http://localhost:8080"
