"""
Core functionality for the AI assistant.
"""

import os
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
import time
import uuid
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

from . import config
from .llm import LLMHandler

@dataclass
class Message:
    """Represents a message in the conversation."""
    role: str  # 'user', 'assistant', or 'system'
    content: str
    timestamp: float
    metadata: Optional[Dict[str, Any]] = None

class Assistant:
    def __init__(self):
        """Initialize the AI assistant with necessary components."""
        self.name = config.ASSISTANT_NAME
        self.conversation_history: List[Message] = []
        
        # Initialize embedding model
        self.embedding_model = SentenceTransformer(config.EMBEDDING_MODEL)
        
        # Initialize vector store
        self.vector_store = chromadb.PersistentClient(
            path=str(config.DATA_DIR / "vectorstore"),
            settings=Settings(
                anonymized_telemetry=False
            )
        )
        
        # Create or get the collection for our knowledge base
        self.knowledge_base = self.vector_store.get_or_create_collection(
            name="knowledge_base",
            metadata={"description": "General knowledge base for the assistant"}
        )
        
        # Initialize LLM handler
        self.llm = LLMHandler()
        
        # Add system prompt to conversation history
        self._add_message("system", config.SYSTEM_PROMPT)
    
    def _add_message(self, role: str, content: str, metadata: Optional[Dict[str, Any]] = None) -> None:
        """Add a message to the conversation history."""
        message = Message(role=role, content=content, timestamp=time.time(), metadata=metadata)
        self.conversation_history.append(message)
    
    def _get_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for a list of texts."""
        return self.embedding_model.encode(texts).tolist()
    
    def _format_messages_for_llm(self) -> List[Dict[str, str]]:
        """Format conversation history for the LLM."""
        return [
            {"role": msg.role, "content": msg.content}
            for msg in self.conversation_history
            if msg.role != "system"  # Exclude system messages as they're handled separately
        ]
    
    def add_to_knowledge_base(self, texts: List[str], metadata: Optional[List[Dict[str, Any]]] = None) -> None:
        """Add texts to the knowledge base."""
        if metadata is None:
            metadata = [{}] * len(texts)
        
        # Generate IDs for the documents
        ids = [str(uuid.uuid4()) for _ in texts]
        
        # Generate embeddings
        embeddings = self._get_embeddings(texts)
        
        # Add to vector store
        self.knowledge_base.add(
            documents=texts,
            embeddings=embeddings,
            metadatas=metadata,
            ids=ids
        )
    
    def query_knowledge_base(self, query: str, n_results: int = 5) -> List[Dict[str, Any]]:
        """Query the knowledge base for relevant information."""
        query_embedding = self._get_embeddings([query])[0]
        
        results = self.knowledge_base.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )
        
        # Format results
        formatted_results = []
        for i in range(len(results['documents'][0])):
            formatted_results.append({
                'text': results['documents'][0][i],
                'metadata': results['metadatas'][0][i],
                'distance': results['distances'][0][i] if 'distances' in results else None
            })
        
        return formatted_results
    
    def process_message(self, message: str) -> str:
        """Process a user message and generate a response."""
        # Add user message to history
        self._add_message("user", message)
        
        try:
            # Query knowledge base for relevant information
            relevant_info = self.query_knowledge_base(message)
            
            # Format context from relevant information
            context = self.llm.format_context(relevant_info)
            
            # Get formatted conversation history
            formatted_messages = self._format_messages_for_llm()
            
            # Generate response using LLM
            response = self.llm.generate_response(
                messages=formatted_messages,
                context=context
            )
            
            # Add assistant response to history
            self._add_message("assistant", response)
            
            return response
            
        except Exception as e:
            error_msg = f"Error processing message: {str(e)}"
            self._add_message("assistant", error_msg)
            return error_msg
    
    def get_conversation_history(self) -> List[Dict[str, Any]]:
        """Get the conversation history in a formatted way."""
        return [
            {
                "role": msg.role,
                "content": msg.content,
                "timestamp": msg.timestamp,
                "metadata": msg.metadata
            }
            for msg in self.conversation_history
        ] 