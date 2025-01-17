"""
Local AI agent with LLM capabilities and MATLAB integration.
"""

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import matlab.engine
import torch
from typing import List, Dict, Optional

class LocalLLMHandler:
    def __init__(self):
        """Initialize the local LLM handler with a smaller model."""
        model_name = "facebook/opt-125m"  # Using a smaller model that's easier to load
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
            low_cpu_mem_usage=True
        ).to(self.device)
        
        # Set up text generation pipeline
        self.generator = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            device=self.device
        )
    
    def generate_response(self, messages: List[Dict[str, str]], max_length: int = 100) -> str:
        """Generate a response using the local LLM."""
        # Format messages into a single string
        prompt = self._format_messages(messages)
        
        # Generate response
        response = self.generator(
            prompt,
            max_length=max_length,
            num_return_sequences=1,
            temperature=0.7,
            do_sample=True
        )[0]["generated_text"]
        
        # Extract only the new content
        return response[len(prompt):].strip()
    
    def _format_messages(self, messages: List[Dict[str, str]]) -> str:
        """Format messages into a string for the model."""
        formatted = ""
        for msg in messages:
            role = msg["role"]
            content = msg["content"]
            if role == "system":
                formatted += f"System: {content}\n"
            elif role == "user":
                formatted += f"User: {content}\n"
            elif role == "assistant":
                formatted += f"Assistant: {content}\n"
        return formatted.strip()

class MatlabTools:
    def __init__(self):
        """Initialize MATLAB engine."""
        self.eng = matlab.engine.start_matlab()
    
    def run_command(self, command: str) -> str:
        """Run a MATLAB command and return the result."""
        try:
            result = self.eng.eval(command, nargout=0)
            return str(result) if result else "Command executed successfully"
        except Exception as e:
            return f"Error executing MATLAB command: {str(e)}"
    
    def analyze_data(self, data: List[float]) -> Dict:
        """Perform basic statistical analysis using MATLAB."""
        try:
            # Convert Python list to MATLAB array
            matlab_array = matlab.double(data)
            
            # Calculate basic statistics
            mean = float(self.eng.mean(matlab_array))
            std = float(self.eng.std(matlab_array))
            median = float(self.eng.median(matlab_array))
            
            return {
                "mean": mean,
                "std": std,
                "median": median
            }
        except Exception as e:
            return {"error": str(e)}

class EnhancedAgent:
    def __init__(self):
        """Initialize the enhanced agent with LLM and MATLAB capabilities."""
        self.llm = LocalLLMHandler()
        self.matlab = MatlabTools()
        
        # Initialize conversation history
        self.conversation_history: List[Dict[str, str]] = [{
            "role": "system",
            "content": "You are a helpful AI assistant with access to MATLAB for computations."
        }]
    
    def process_query(self, query: str) -> str:
        """Process a user query and generate a response."""
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": query
        })
        
        # Generate response
        response = self.llm.generate_response(self.conversation_history)
        
        # Add assistant response to history
        self.conversation_history.append({
            "role": "assistant",
            "content": response
        })
        
        return response
    
    def run_matlab_analysis(self, data: List[float]) -> Dict:
        """Run statistical analysis using MATLAB."""
        return self.matlab.analyze_data(data)
    
    def get_conversation_history(self) -> List[Dict[str, str]]:
        """Return the conversation history."""
        return self.conversation_history 