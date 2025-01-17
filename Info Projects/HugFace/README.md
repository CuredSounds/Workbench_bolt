# Sentiment Analysis with Hugging Face 🤗

A powerful sentiment analysis application built using Hugging Face Transformers and Streamlit. This project demonstrates how to use pre-trained transformer models for natural language processing tasks.

## Features
- Real-time sentiment analysis of text input
- Confidence scoring for predictions
- Beautiful Streamlit web interface
- BERT-based model for accurate sentiment detection
- Caching for improved performance

## Installation

### Prerequisites
- Python 3.8+
- Conda environment

### Setup
1. Clone this repository
2. Create and activate the Conda environment:
```bash
conda create -n sentiment_env python=3.8
conda activate sentiment_env
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Environment Variables
Create a `.env` file with your Hugging Face token:
```
HUGGINGFACE_TOKEN=your_token_here
```

## Usage
Run the application:
```bash
streamlit run sentiment_analyzer.py
```

The web interface will open automatically in your default browser.

## How It Works
The application uses a BERT-based transformer model from Hugging Face's model hub for sentiment analysis. The model has been trained on a large dataset to recognize emotional tone in text.

Key components:
- `transformers`: For accessing pre-trained models
- `streamlit`: For the web interface
- `torch`: Deep learning backend
- `pipeline`: Hugging Face's abstraction for easy model usage

## Project Structure
```
.
├── README.md
├── requirements.txt
├── sentiment_analyzer.py
└── .env
```

## Tips for Best Results
- Use clear, complete sentences
- Try different lengths of text
- Compare results for different phrasings
- Input text should be in English

## Advanced Usage
The model returns:
- Sentiment label (POSITIVE/NEGATIVE)
- Confidence score (0-100%)

Example:
```python
from transformers import pipeline
classifier = pipeline("sentiment-analysis")
result = classifier("I love this project!")
print(result)  # [{'label': 'POSITIVE', 'score': 0.9998}]
```

## Contributing
Feel free to open issues or submit pull requests for improvements.

## License
MIT License

## Acknowledgments
- Hugging Face for the transformers library
- Streamlit for the web framework 
