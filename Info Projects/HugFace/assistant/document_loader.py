"""
Document loader module for handling different file types.
"""

from typing import List, Dict, Any, Optional
from pathlib import Path
import pypdf
from docx import Document
import requests
from bs4 import BeautifulSoup
from langchain.text_splitter import RecursiveCharacterTextSplitter

from . import config

class DocumentLoader:
    def __init__(self):
        """Initialize the document loader with text splitting capabilities."""
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.CHUNK_SIZE,
            chunk_overlap=config.CHUNK_OVERLAP,
            length_function=len,
        )
    
    def load_pdf(self, file_path: str) -> List[Dict[str, Any]]:
        """
        Load and process a PDF file.
        
        Args:
            file_path: Path to the PDF file
            
        Returns:
            List of dictionaries containing text chunks and metadata
        """
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"PDF file not found: {file_path}")
        
        # Read PDF
        with open(path, 'rb') as file:
            pdf = pypdf.PdfReader(file)
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        
        # Split text into chunks
        chunks = self.text_splitter.split_text(text)
        
        # Prepare metadata
        metadata = {
            "source": str(path),
            "type": "pdf",
            "title": path.stem
        }
        
        return [
            {"text": chunk, "metadata": metadata}
            for chunk in chunks
        ]
    
    def load_docx(self, file_path: str) -> List[Dict[str, Any]]:
        """
        Load and process a Word document.
        
        Args:
            file_path: Path to the Word document
            
        Returns:
            List of dictionaries containing text chunks and metadata
        """
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Word document not found: {file_path}")
        
        # Read Word document
        doc = Document(path)
        text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        
        # Split text into chunks
        chunks = self.text_splitter.split_text(text)
        
        # Prepare metadata
        metadata = {
            "source": str(path),
            "type": "docx",
            "title": path.stem
        }
        
        return [
            {"text": chunk, "metadata": metadata}
            for chunk in chunks
        ]
    
    def load_text(self, file_path: str) -> List[Dict[str, Any]]:
        """
        Load and process a text file.
        
        Args:
            file_path: Path to the text file
            
        Returns:
            List of dictionaries containing text chunks and metadata
        """
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Text file not found: {file_path}")
        
        # Read text file
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Split text into chunks
        chunks = self.text_splitter.split_text(text)
        
        # Prepare metadata
        metadata = {
            "source": str(path),
            "type": "text",
            "title": path.stem
        }
        
        return [
            {"text": chunk, "metadata": metadata}
            for chunk in chunks
        ]
    
    def load_url(self, url: str) -> List[Dict[str, Any]]:
        """
        Load and process content from a URL.
        
        Args:
            url: Web page URL to process
            
        Returns:
            List of dictionaries containing text chunks and metadata
        """
        try:
            # Fetch webpage
            response = requests.get(url)
            response.raise_for_status()
            
            # Parse HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Remove script and style elements
            for element in soup(['script', 'style']):
                element.decompose()
            
            # Get text content
            text = soup.get_text(separator='\n')
            
            # Split text into chunks
            chunks = self.text_splitter.split_text(text)
            
            # Prepare metadata
            metadata = {
                "source": url,
                "type": "url",
                "title": soup.title.string if soup.title else url
            }
            
            return [
                {"text": chunk, "metadata": metadata}
                for chunk in chunks
            ]
            
        except Exception as e:
            raise ValueError(f"Error loading URL {url}: {str(e)}")
    
    def load_file(self, file_path: str) -> List[Dict[str, Any]]:
        """
        Load any supported file type based on extension.
        
        Args:
            file_path: Path to the file
            
        Returns:
            List of dictionaries containing text chunks and metadata
        """
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Determine file type and use appropriate loader
        extension = path.suffix.lower()
        if extension == '.pdf':
            return self.load_pdf(file_path)
        elif extension == '.docx':
            return self.load_docx(file_path)
        elif extension in ['.txt', '.md', '.py', '.json', '.yaml', '.yml']:
            return self.load_text(file_path)
        else:
            raise ValueError(f"Unsupported file type: {extension}") 