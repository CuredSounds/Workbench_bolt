# Download Stable Diffusion model using Hugging Face API key
Write-Host "Downloading Stable Diffusion model..." -ForegroundColor Green

# Load Hugging Face API key from .env
$envContent = Get-Content .env
$hfKey = $envContent | Where-Object { $_ -match "HUGGINGFACE_API_KEY=(.*)" } | ForEach-Object { $matches[1] }

if (-not $hfKey) {
    Write-Host "Error: Hugging Face API key not found in .env file" -ForegroundColor Red
    exit 1
}

# Set up paths
$modelDir = "stable-diffusion/stable-diffusion-webui/models/Stable-diffusion"
$modelPath = "$modelDir/v1-5-pruned-emaonly.safetensors"
$modelUrl = "https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors"

# Create directory if it doesn't exist
if (-not (Test-Path $modelDir)) {
    New-Item -ItemType Directory -Path $modelDir -Force | Out-Null
}

Write-Host "Starting download..." -ForegroundColor Yellow
Write-Host "This may take a while depending on your internet speed." -ForegroundColor Yellow
Write-Host "Model size is approximately 4GB." -ForegroundColor Yellow

try {
    Write-Host "Downloading model file... (This may take a while)" -ForegroundColor Yellow
    
    $webClient = New-Object System.Net.WebClient
    $webClient.Headers.Add("Authorization", "Bearer $hfKey")
    $webClient.DownloadFile($modelUrl, "$modelPath")
    
    Write-Host "Download completed successfully!" -ForegroundColor Green
    
} catch {
    Write-Host "Error downloading model: $_" -ForegroundColor Red
    exit 1
}

Write-Host "`nModel downloaded successfully to: $modelPath" -ForegroundColor Green
Write-Host "You can now run '.\start-all-services.ps1' to start the AI services" -ForegroundColor Cyan
