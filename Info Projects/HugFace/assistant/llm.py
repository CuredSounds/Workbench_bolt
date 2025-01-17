"""
LLM integration module for the AI assistant.
"""

from typing import List, Dict, Any, Optional
import openai
from . import config

class LLMHandler:
    def __init__(self):
        """Initialize the LLM handler with API keys."""
        openai.api_key = config.OPENAI_API_KEY
        
        if not openai.api_key:
            raise ValueError("OpenAI API key not found in environment variables")
    
    def generate_response(
        self,
        messages: List[Dict[str, str]],
        context: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 500
    ) -> str:
        """
        Generate a response using the OpenAI API.
        
        Args:
            messages: List of conversation messages in OpenAI format
            context: Additional context from knowledge base
            temperature: Controls randomness (0.0 to 1.0)
            max_tokens: Maximum length of the response
            
        Returns:
            str: Generated response
        """
        # Prepare the messages
        formatted_messages = []
        
        # Add system message with context if provided
        system_message = config.SYSTEM_PROMPT
        if context:
            system_message += f"\n\nRelevant context:\n{context}"
        formatted_messages.append({"role": "system", "content": system_message})
        
        # Add conversation history
        formatted_messages.extend(messages)
        
        try:
            response = openai.chat.completions.create(
                model=config.COMPLETION_MODEL,
                messages=formatted_messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def format_context(self, relevant_info: List[Dict[str, Any]]) -> str:
        """Format relevant information into a context string."""
        if not relevant_info:
            return ""
        
        context = "Here is some relevant information from my knowledge base:\n\n"
        for info in relevant_info:
            context += f"- {info['text']}\n"
        return context 