"""
Configuration settings for the personal assistant.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

# Paths
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"
CACHE_DIR = BASE_DIR / "cache"

# Create directories if they don't exist
for dir_path in [DATA_DIR, MODELS_DIR, CACHE_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)

# Model Settings
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
COMPLETION_MODEL = "gpt-3.5-turbo"  # OpenAI model for completions

# RAG Settings
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# Assistant Settings
ASSISTANT_NAME = "Luna"
SYSTEM_PROMPT = f"""You are {ASSISTANT_NAME}, a helpful and knowledgeable AI assistant. 
You have access to various tools and can help with tasks like:
- Answering questions using your knowledge base
- Processing and analyzing documents
- Searching the internet for information
- Managing files and data
- Running local machine learning models

Always be clear about your capabilities and limitations. If you're unsure about something,
say so directly. When using external tools or APIs, explain what you're doing.""" 