
# Setup-Stable-Diffusion.ps1
# Script to install and configure Stable Diffusion Web UI

Write-Host "Setting up Stable Diffusion Web UI..." -ForegroundColor Green

# Create stable-diffusion directory if it doesn't exist
$sdDir = "stable-diffusion"
if (-not (Test-Path $sdDir)) {
    Write-Host "Creating Stable Diffusion directory..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Path $sdDir | Out-Null
}
Set-Location $sdDir

# Install Python 3.10 using winget
Write-Host "Installing Python 3.10..." -ForegroundColor Yellow
winget install Python.Python.3.10

# Verify Python 3.10 installation
$python310Path = "C:\Users\brent\AppData\Local\Programs\Python\Python310\python.exe"
if (-not (Test-Path $python310Path)) {
    Write-Host "Error: Python 3.10 installation not found" -ForegroundColor Red
    exit 1
}

# Create virtual environment
Write-Host "Creating Python virtual environment..." -ForegroundColor Yellow
& $python310Path -m venv venv
$venvPython = ".\venv\Scripts\python.exe"
$venvPip = ".\venv\Scripts\pip.exe"

# Install required packages
Write-Host "Installing required packages..." -ForegroundColor Yellow
& $venvPip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
& $venvPip install numpy

# Remove existing webui directory if it exists
if (Test-Path "stable-diffusion-webui") {
    Write-Host "Removing existing Stable Diffusion Web UI..." -ForegroundColor Yellow
    Remove-Item -Path "stable-diffusion-webui" -Recurse -Force
}

# Clone Automatic1111 repository
Write-Host "Cloning Stable Diffusion Web UI repository..." -ForegroundColor Yellow
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git

# Verify the clone was successful
if (-not (Test-Path "stable-diffusion-webui")) {
    Write-Host "Error: Failed to clone repository" -ForegroundColor Red
    exit 1
}

# Change to webui directory
Set-Location "stable-diffusion-webui"

# Create or update webui-user.bat with optimized settings
$webuiContent = @"
@echo off
set PYTHON=C:\Users\brent\AppData\Local\Programs\Python\Python310\python.exe
set GIT=
set VENV_DIR=
set COMMANDLINE_ARGS=--xformers --api --listen --port 7860 --precision full --no-half --medvram --opt-split-attention
"@
Set-Content -Path "webui-user.bat" -Value $webuiContent

# Create models directory if it doesn't exist
if (-not (Test-Path "models\Stable-diffusion")) {
    New-Item -ItemType Directory -Path "models\Stable-diffusion" -Force | Out-Null
    
    # Check if model exists in parent directory
    $existingModelDir = "..\..\stable-diffusion-v1-5"
    if (Test-Path $existingModelDir) {
        Write-Host "Found existing model directory. Copying models..." -ForegroundColor Yellow
        Copy-Item "$existingModelDir\*" "models\Stable-diffusion\" -Recurse
        Write-Host "Models copied successfully" -ForegroundColor Green
    }
}

Write-Host "`nStable Diffusion Web UI setup complete!" -ForegroundColor Green
Write-Host "Next step:" -ForegroundColor Cyan
Write-Host "Run '.\start-all-services.ps1' to download the model and start all services" -ForegroundColor Cyan

# Return to original directory
Set-Location ..\..
