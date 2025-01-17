import requests
import os
from typing import Dict, Union, List
import time

class HuggingFaceTextSummarizer:
    """A class to handle text summarization using Hugging Face's BART-large-CNN model."""
    
    def __init__(self, api_key: str = None):
        """
        Initialize the summarizer with API credentials.
        
        Args:
            api_key (str, optional): Hugging Face API key. If not provided, looks for 'HUGGINGFACE_API_KEY' in environment variables.
        """
        self.API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        self.api_key = api_key or os.getenv('HUGGINGFACE_API_KEY')
        if not self.api_key:
            raise ValueError("API key must be provided either directly or through HUGGINGFACE_API_KEY environment variable")
        
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def query(self, payload: Dict) -> Union[Dict, List]:
        """
        Send a query to the Hugging Face API.
        
        Args:
            payload (Dict): The input payload containing the text to summarize.
            
        Returns:
            Union[Dict, List]: The API response containing the summary.
            
        Raises:
            requests.exceptions.RequestException: If the API request fails.
        """
        max_retries = 3
        retry_delay = 1  # seconds

        for attempt in range(max_retries):
            try:
                response = requests.post(self.API_URL, headers=self.headers, json=payload)
                response.raise_for_status()  # Raise an exception for bad status codes
                return response.json()
            except requests.exceptions.RequestException as e:
                if attempt == max_retries - 1:  # Last attempt
                    raise
                print(f"Attempt {attempt + 1} failed. Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
                retry_delay *= 2  # Exponential backoff

    def summarize(self, text: str, max_length: int = 130, min_length: int = 30) -> str:
        """
        Summarize the given text using the BART model.
        
        Args:
            text (str): The text to summarize.
            max_length (int, optional): Maximum length of the summary. Defaults to 130.
            min_length (int, optional): Minimum length of the summary. Defaults to 30.
            
        Returns:
            str: The generated summary.
        """
        if not text.strip():
            raise ValueError("Input text cannot be empty")

        payload = {
            "inputs": text,
            "parameters": {
                "max_length": max_length,
                "min_length": min_length,
                "do_sample": False
            }
        }

        try:
            response = self.query(payload)
            if isinstance(response, list) and len(response) > 0:
                return response[0].get('summary_text', '')
            return ''
        except Exception as e:
            raise Exception(f"Failed to generate summary: {str(e)}")


def main():
    # Example usage
    sample_text = """The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, 
    and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. 
    During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest 
    man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York 
    City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the 
    addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler 
    Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest 
    free-standing structure in France after the Millau Viaduct."""

    try:
        summarizer = HuggingFaceTextSummarizer()
        summary = summarizer.summarize(sample_text)
        print("Summary:", summary)
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main() 