# Live Agent Studio Development Guide

This repository contains comprehensive documentation and setup guides for developing agents for the Live Agent Studio platform. Each section is detailed in its own README within the respective directories.

## Project Structure

```
live-agent-studio/
├── docs/                           # Documentation directory
│   ├── n8n-agents/                # n8n agent development guides
│   ├── python-agents/             # Python agent development guides
│   ├── database/                  # Database setup and schemas
│   ├── docker/                    # Docker configuration guides
│   └── testing/                   # Testing procedures and guides
├── templates/                      # Agent templates
│   ├── n8n/                       # n8n agent templates
│   └── python/                    # Python agent templates
├── infrastructure/                 # Infrastructure setup
│   ├── docker/                    # Docker configurations
│   └── database/                  # Database migrations
├── examples/                      # Example agents
│   ├── n8n-examples/             # n8n agent examples
│   └── python-examples/          # Python agent examples
└── tools/                        # Development tools and scripts
```

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/yourusername/live-agent-studio.git
cd live-agent-studio
```

2. Choose your agent type:
   - [N8n Agent Development Guide](docs/n8n-agents/README.md)
   - [Python Agent Development Guide](docs/python-agents/README.md)

3. Set up infrastructure:
   - [Docker Setup Guide](docs/docker/README.md)
   - [Database Setup Guide](docs/database/README.md)

4. Start development:
   - Use templates from `templates/` directory
   - Follow testing guidelines in `docs/testing/`
   - Reference examples in `examples/` directory

## Documentation Index

1. [N8n Agent Development](docs/n8n-agents/README.md)
   - Workflow setup
   - Node configuration
   - Webhook integration
   - Database integration

2. [Python Agent Development](docs/python-agents/README.md)
   - FastAPI setup
   - Agent implementation
   - Database integration
   - Docker containerization

3. [Database Setup](docs/database/README.md)
   - Schema design
   - Migrations
   - Vector storage
   - Performance optimization

4. [Docker Configuration](docs/docker/README.md)
   - Base images
   - Development environment
   - Production deployment
   - Multi-stage builds

5. [Testing Procedures](docs/testing/README.md)
   - Unit testing
   - Integration testing
   - Load testing
   - Security testing

## Prerequisites

- Python 3.11+
- Docker
- n8n (for n8n agents)
- PostgreSQL or Supabase account
- Node.js 16+ (for n8n development)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - see [LICENSE](LICENSE) for details

## Support

- [Documentation](https://studio.ottomator.ai/guide)
- [Community Forum](https://thinktank.ottomator.ai)
- [Issue Tracker](https://github.com/yourusername/live-agent-studio/issues)
