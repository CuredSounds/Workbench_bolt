# Pydantic AI Advanced Researcher - Build Guide

This guide will help you set up and run the Pydantic AI Advanced Researcher project.

## 1. Environment Setup

### Prerequisites
```bash
# Required software
- Python 3.11+
- pip (Python package manager)
- git
- virtualenv or venv
```

### Initial Setup
```bash
# Clone the repository (if not already done)
git clone https://github.com/yourusername/ottomator-agents.git
cd ottomator-agents/pydantic-ai-advanced-researcher

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Unix/MacOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 2. Configuration

### Environment Variables
1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` with your credentials:
```env
OPENAI_API_KEY=your_openai_api_key  # Required for GPT models
BRAVE_API_KEY=your_brave_api_key    # Required for web search
LLM_MODEL=gpt-4o                    # Or your preferred model
```

## 3. Running the Agent

### Command Line Interface
```bash
# Run the basic web search agent
python web_search_agent.py
```

### Streamlit Interface
```bash
# Run the web interface
streamlit run streamlit_ui.py
```

## 4. Development Workflow

### Project Structure
```
pydantic-ai-advanced-researcher/
├── web_search_agent.py         # Core agent implementation
├── streamlit_ui.py            # Web interface
├── requirements.txt           # Project dependencies
└── .env                      # Configuration file
```

### Making Changes
1. Core Agent (`web_search_agent.py`):
   - Modify search parameters
   - Add new tools/capabilities
   - Adjust model settings

2. Web Interface (`streamlit_ui.py`):
   - Customize UI components
   - Add new features
   - Modify chat interface

## 5. Testing

### Manual Testing
```bash
# Test core functionality
python web_search_agent.py

# Test web interface
streamlit run streamlit_ui.py
```

### Common Test Cases
1. Basic web search
2. Complex queries
3. Error handling
4. API limits
5. Model responses

## 6. Troubleshooting

### Common Issues

1. **API Key Issues**
```bash
# Check environment variables
echo $OPENAI_API_KEY
echo $BRAVE_API_KEY
```

2. **Model Issues**
- Verify model name in `.env`
- Check API access
- Monitor rate limits

3. **Search Issues**
- Verify Brave API key
- Check query formatting
- Monitor API response

## 7. Next Steps

1. **Customization**
   - Add custom search filters
   - Implement additional APIs
   - Enhance response formatting

2. **Integration**
   - Add database storage
   - Implement caching
   - Add authentication

3. **Deployment**
   - Set up Docker
   - Configure production env
   - Add monitoring

## 8. Resources

- [Pydantic AI Documentation](https://docs.pydantic.dev/)
- [Brave Search API Docs](https://brave.com/search/api/)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Streamlit Documentation](https://docs.streamlit.io/) 