"""
Personal AI Assistant with RAG capabilities.
"""

from .core import Assistant
from .cli import AssistantCLI

__version__ = "0.1.0"
__all__ = ["Assistant", "AssistantCLI"] 