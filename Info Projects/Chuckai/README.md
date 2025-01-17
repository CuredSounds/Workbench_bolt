# Chuckai - Local AI Development Environment

A comprehensive local AI development environment that includes:
- Local Large Language Models (via Ollama)
- Web-based Chat Interface (via Open WebUI)
- Image Generation (via Stable Diffusion)

## System Requirements

### Minimum Requirements
- Any computer running Windows, Mac, or Linux
- GPU recommended but not required
- WSL2 required for Windows users

### Recommended Hardware (based on usage)
For basic LLM usage:
- 16GB+ RAM
- Modern CPU (8+ cores)
- NVIDIA GPU with 8GB+ VRAM

For optimal performance with image generation:
- 32GB+ RAM
- Modern CPU (12+ cores)
- NVIDIA GPU with 12GB+ VRAM

## Components

### 1. Ollama
Base foundation for running AI models locally. Supports various models including:
- Llama 2
- CodeGemma
- And many more from ollama.ai

### 2. Open WebUI
Feature-rich web interface for interacting with AI models:
- Chat interface with conversation history
- Multiple model support
- File upload and analysis
- User management and permissions
- Custom model configurations

### 3. Stable Diffusion (Optional)
Local image generation capabilities:
- Text-to-image generation
- Integration with Open WebUI
- Custom model support
- Fast local processing

## Setup Instructions

### Windows Setup

1. Install WSL2:
```bash
wsl --install
```

2. Install Ollama:
```bash
curl https://ollama.ai/install.sh | sh
```

3. Install Docker for Open WebUI:
```bash
# Update package list
sudo apt-get update

# Install Docker dependencies
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common

# Add Docker's official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# Add Docker repository
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# Install Docker
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io
```

4. Deploy Open WebUI:
```bash
sudo docker run -d \
  --name open-webui \
  --network host \
  -v open-webui:/app/backend/data \
  -e OLLAMA_BASE_URL=http://127.0.0.1:11434 \
  --restart unless-stopped \
  ghcr.io/open-webui/open-webui:main
```

### Mac/Linux Setup

1. Install Ollama:
```bash
curl https://ollama.ai/install.sh | sh
```

2. Follow Docker and Open WebUI installation steps from Windows section above (skip WSL2 part)

## Usage

1. Access the web interface at: http://localhost:8080

2. First-time setup:
   - Create an admin account
   - Configure available models
   - Set up user permissions if needed

3. Pull and run models:
```bash
ollama pull llama2
ollama run llama2
```

## Security Considerations

1. API Keys and Sensitive Data:
   - Store API keys in a secure .env file
   - Never commit sensitive data to version control
   - Use the provided .gitignore file

2. User Management:
   - Enable user registration restrictions
   - Set appropriate model access permissions
   - Monitor chat histories when needed

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Based on the excellent work of Network Chuck
- Uses various open-source projects including Ollama, Open WebUI, and Stable Diffusion
