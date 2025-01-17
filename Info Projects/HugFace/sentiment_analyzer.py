"""
Sentiment Analysis Application using TextBlob
-----------------------------------------------------------
This application provides real-time sentiment analysis using TextBlob.
It features a user-friendly web interface built with Streamlit.

Author: Your Name
License: MIT
"""

import os
import streamlit as st
from textblob import TextBlob
from typing import Dict, Any

# Set up page configuration
st.set_page_config(
    page_title="Sentiment Analyzer",
    page_icon="🤗",
    layout="centered"
)

# Styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTextArea {
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

def analyze_sentiment(text: str) -> Dict[str, Any]:
    """
    Analyze the sentiment of given text using TextBlob.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        dict: Sentiment analysis results including polarity and subjectivity
    """
    analysis = TextBlob(text)
    # Convert polarity to sentiment label
    if analysis.sentiment.polarity > 0:
        sentiment = "POSITIVE"
    elif analysis.sentiment.polarity < 0:
        sentiment = "NEGATIVE"
    else:
        sentiment = "NEUTRAL"
    
    # Convert polarity to percentage (0-100%)
    confidence = (abs(analysis.sentiment.polarity) + 1) / 2
    
    return {
        "label": sentiment,
        "score": confidence,
        "polarity": analysis.sentiment.polarity,
        "subjectivity": analysis.sentiment.subjectivity
    }

# Create header
st.title("🤗 Sentiment Analysis")
st.write("Enter text below for real-time sentiment analysis!")

# Create text input with character counter
text_input = st.text_area(
    "Enter text to analyze:",
    height=100,
    max_chars=512,
    help="Maximum 512 characters"
)

# Add analysis options
with st.expander("Advanced Options"):
    show_details = st.checkbox("Show technical details", value=False)

if text_input:
    with st.spinner("Analyzing sentiment..."):
        try:
            # Perform sentiment analysis
            result = analyze_sentiment(text_input)
            sentiment = result['label']
            score = result['score']

            # Display results
            st.write("### Results")
            
            # Display sentiment with color coding
            if sentiment == "POSITIVE":
                st.success(f"Sentiment: {sentiment} (Confidence: {score:.2%})")
            elif sentiment == "NEGATIVE":
                st.error(f"Sentiment: {sentiment} (Confidence: {score:.2%})")
            else:
                st.info(f"Sentiment: {sentiment} (Confidence: {score:.2%})")
            
            # Show technical details if requested
            if show_details:
                st.write("### Technical Details")
                st.json({
                    "text_length": len(text_input),
                    "polarity": result['polarity'],
                    "subjectivity": result['subjectivity'],
                    "raw_score": score,
                })

        except Exception as e:
            st.error(f"Error during analysis: {str(e)}")

# Add explanation
with st.expander("How it works"):
    st.write("""
    This application uses TextBlob's natural language processing capabilities to analyze the 
    emotional tone of text. It provides both sentiment (POSITIVE/NEGATIVE/NEUTRAL) and 
    additional metrics like polarity and subjectivity scores.
    
    - Polarity: Measures how positive or negative the text is (-1 to 1)
    - Subjectivity: Measures how subjective or objective the text is (0 to 1)
    """)

# Add footer with instructions
st.markdown("---")
st.markdown("""
### Tips for best results:
- Try different lengths of text (up to 512 characters)
- Use clear, complete sentences
- Compare results for different phrasings
- Check technical details for more insight
""")

# Add version information
st.sidebar.markdown("### About")
st.sidebar.info("""
Version: 1.0.0
Model: TextBlob
Framework: NLTK
""") 