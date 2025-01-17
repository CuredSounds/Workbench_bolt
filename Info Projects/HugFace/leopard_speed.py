"""
Interactive CLI for asking questions using smolagents.
"""

from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
from rich.console import Console
from rich.markdown import Markdown

console = Console()

def create_agent():
    """Create and return a configured agent."""
    return CodeAgent(
        tools=[DuckDuckGoSearchTool()],
        model=HfApiModel()
    )

def main():
    console.print("[bold green]Welcome to the Interactive Question Answering System![/bold green]")
    console.print("[dim]Type 'exit' to quit the program[/dim]\n")
    
    # Initialize the agent
    agent = create_agent()
    
    while True:
        # Get user input
        console.print("[bold cyan]Ask a question:[/bold cyan]")
        question = input("> ").strip()
        
        # Check for exit command
        if question.lower() in ('exit', 'quit'):
            console.print("\n[yellow]Goodbye![/yellow]")
            break
        
        # Skip empty questions
        if not question:
            console.print("[yellow]Please enter a valid question.[/yellow]")
            continue
        
        try:
            # Process the question
            console.print("\n[dim]Thinking...[/dim]")
            response = agent.run(question)
            
            # Display the response
            console.print("\n[bold green]Answer:[/bold green]")
            console.print(Markdown(str(response)))
            console.print()  # Empty line for readability
            
        except Exception as e:
            console.print(f"[red]Error processing question: {str(e)}[/red]")
        
        console.print("[dim]---[/dim]\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]Goodbye![/yellow]") 