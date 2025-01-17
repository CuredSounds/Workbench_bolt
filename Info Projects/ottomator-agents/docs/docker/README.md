# Docker Configuration Guide

This guide covers Docker setup and configuration for Live Agent Studio agents.

## Base Images

### 1. Python Base Image
```dockerfile
# Base Python image for agents
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m -u 1000 agent

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Switch to non-root user
USER agent

# Expose default port
EXPOSE 8001

# Default command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
```

### 2. N8n Base Image
```dockerfile
FROM n8nio/n8n:latest

# Add custom dependencies if needed
USER root
RUN apt-get update && apt-get install -y \
    your-package-here \
    && rm -rf /var/lib/apt/lists/*

# Switch back to n8n user
USER node

# Copy workflows
COPY workflows /home/node/.n8n/workflows/
```

## Development Environment

1. **Docker Compose Setup**
```yaml
version: '3.8'

services:
  agent:
    build: .
    ports:
      - "8001:8001"
    volumes:
      - .:/app
    env_file:
      - .env
    depends_on:
      - db

  db:
    image: postgres:14
    environment:
      POSTGRES_USER: agent_user
      POSTGRES_PASSWORD: your_password
      POSTGRES_DB: live_agent_studio
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

2. **Development Commands**
```bash
# Build and start services
docker-compose up -d --build

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

## Production Deployment

### Multi-stage Builds
```dockerfile
# Build stage
FROM python:3.11-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.11-slim

WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
```

### Production Configuration
```yaml
version: '3.8'

services:
  agent:
    build:
      context: .
      dockerfile: Dockerfile.prod
    restart: unless-stopped
    environment:
      - ENVIRONMENT=production
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 1G
```

## Resource Management

1. **Memory Limits**
   - Set container limits
   - Monitor usage
   - Handle OOM errors
   - Optimize allocations

2. **CPU Allocation**
   - Set CPU shares
   - Monitor usage
   - Performance tuning
   - Load balancing

3. **Storage**
   - Volume management
   - Cleanup policies
   - Backup strategies
   - Performance optimization

## Monitoring

1. **Container Health**
   - Health checks
   - Resource monitoring
   - Log aggregation
   - Alert configuration

2. **Performance Metrics**
   - CPU usage
   - Memory usage
   - Network I/O
   - Disk I/O

## Security

1. **Image Security**
   - Use official base images
   - Regular updates
   - Vulnerability scanning
   - Minimal dependencies

2. **Runtime Security**
   - Non-root user
   - Read-only filesystem
   - Limited capabilities
   - Network isolation

## Troubleshooting

Common issues and solutions:
1. Build failures
2. Container crashes
3. Resource exhaustion
4. Network issues

## Resources

- [Docker Documentation](https://docs.docker.com)
- [Docker Compose Documentation](https://docs.docker.com/compose)
- [Docker Hub](https://hub.docker.com)
- [Docker Security](https://docs.docker.com/engine/security) 