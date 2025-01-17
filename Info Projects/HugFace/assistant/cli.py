"""
Command-line interface for the AI assistant.
"""

import cmd
import sys
from typing import Optional
from pathlib import Path
from rich.console import Console
from rich.markdown import Markdown
from . import config
from .core import Assistant
from .document_loader import DocumentLoader

console = Console()

class AssistantCLI(cmd.Cmd):
    intro = 'Welcome to your AI Assistant! Type help or ? to list commands.\n'
    prompt = '> '
    
    def __init__(self):
        super().__init__()
        self.assistant = Assistant()
        self.document_loader = DocumentLoader()
        console.print(f"[bold green]Initializing {self.assistant.name}...[/bold green]")
    
    def do_chat(self, arg: str) -> None:
        """Send a message to the assistant: chat <your message>"""
        if not arg:
            console.print("[yellow]Please provide a message.[/yellow]")
            return
        
        with console.status("[bold green]Thinking...[/bold green]"):
            response = self.assistant.process_message(arg)
        
        console.print(f"\n[bold cyan]{self.assistant.name}:[/bold cyan] ", end="")
        console.print(Markdown(response))
        console.print()
    
    def do_add(self, arg: str) -> None:
        """Add text to the knowledge base: add <text>"""
        if not arg:
            console.print("[yellow]Please provide text to add.[/yellow]")
            return
        
        with console.status("[bold green]Adding to knowledge base...[/bold green]"):
            self.assistant.add_to_knowledge_base([arg])
        console.print("[green]Added to knowledge base.[/green]")
    
    def do_load(self, arg: str) -> None:
        """Load a document into the knowledge base: load <file_path>"""
        if not arg:
            console.print("[yellow]Please provide a file path.[/yellow]")
            return
        
        try:
            path = Path(arg)
            with console.status(f"[bold green]Loading {path.name}...[/bold green]"):
                chunks = self.document_loader.load_file(arg)
                texts = [chunk["text"] for chunk in chunks]
                metadata = [chunk["metadata"] for chunk in chunks]
                self.assistant.add_to_knowledge_base(texts, metadata)
            
            console.print(f"[green]Successfully loaded {path.name} into knowledge base.[/green]")
            console.print(f"[dim]Split into {len(chunks)} chunks.[/dim]")
            
        except Exception as e:
            console.print(f"[red]Error loading file: {str(e)}[/red]")
    
    def do_loadurl(self, arg: str) -> None:
        """Load content from a URL into the knowledge base: loadurl <url>"""
        if not arg:
            console.print("[yellow]Please provide a URL.[/yellow]")
            return
        
        try:
            with console.status(f"[bold green]Loading content from URL...[/bold green]"):
                chunks = self.document_loader.load_url(arg)
                texts = [chunk["text"] for chunk in chunks]
                metadata = [chunk["metadata"] for chunk in chunks]
                self.assistant.add_to_knowledge_base(texts, metadata)
            
            console.print("[green]Successfully loaded URL content into knowledge base.[/green]")
            console.print(f"[dim]Split into {len(chunks)} chunks.[/dim]")
            
        except Exception as e:
            console.print(f"[red]Error loading URL: {str(e)}[/red]")
    
    def do_history(self, arg: str) -> None:
        """Show conversation history"""
        history = self.assistant.get_conversation_history()
        for msg in history:
            if msg['role'] != 'system':  # Skip system messages
                role_color = "cyan" if msg['role'] == "assistant" else "green"
                console.print(f"\n[bold {role_color}]{msg['role'].upper()}:[/bold {role_color}] ", end="")
                console.print(Markdown(msg['content']))
    
    def do_clear(self, arg: str) -> None:
        """Clear the console screen"""
        console.clear()
        console.print(self.intro)
    
    def do_quit(self, arg: str) -> bool:
        """Exit the assistant"""
        console.print("\n[yellow]Goodbye![/yellow]")
        return True
    
    def do_EOF(self, arg: str) -> bool:
        """Exit on Ctrl-D (EOF)"""
        return self.do_quit(arg)

def main():
    try:
        AssistantCLI().cmdloop()
    except KeyboardInterrupt:
        console.print("\n[yellow]Goodbye![/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)

if __name__ == '__main__':
    main() 