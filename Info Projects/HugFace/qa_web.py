"""
Streamlit web interface for the AI assistant with LLM and MATLAB integration.
"""

import streamlit as st
import numpy as np
from local_agent import EnhancedAgent
import time

def initialize_session_state():
    """Initialize session state variables."""
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'agent' not in st.session_state:
        st.session_state.agent = EnhancedAgent()

def main():
    st.set_page_config(
        page_title="Enhanced AI Assistant",
        page_icon="🤖",
        layout="wide"
    )
    
    # Initialize session state
    initialize_session_state()
    
    # Header
    st.title("🤖 Enhanced AI Assistant")
    st.markdown("""
    This AI assistant combines:
    - Local Language Model for text generation
    - MATLAB integration for numerical computations
    - Conversation history tracking
    """)
    
    # Create tabs for different functionalities
    qa_tab, matlab_tab = st.tabs(["Q&A", "MATLAB Analysis"])
    
    # Q&A Tab
    with qa_tab:
        question = st.text_area("Ask a question:", height=100)
        
        if st.button("Send", type="primary"):
            if not question:
                st.warning("Please enter a question.")
            else:
                with st.spinner("Thinking..."):
                    try:
                        # Get response from agent
                        response = st.session_state.agent.process_query(question)
                        
                        # Display the answer
                        st.success("Answer:")
                        st.markdown(response)
                        
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
    
    # MATLAB Analysis Tab
    with matlab_tab:
        st.subheader("Statistical Analysis")
        data_input = st.text_area(
            "Enter numbers (comma-separated):",
            placeholder="1.0, 2.0, 3.0, 4.0, 5.0"
        )
        
        if st.button("Analyze", type="primary"):
            if not data_input:
                st.warning("Please enter some numbers.")
            else:
                try:
                    # Parse input data
                    data = [float(x.strip()) for x in data_input.split(",")]
                    
                    # Run analysis
                    results = st.session_state.agent.run_matlab_analysis(data)
                    
                    # Display results
                    if "error" in results:
                        st.error(results["error"])
                    else:
                        st.success("Analysis Results:")
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Mean", f"{results['mean']:.2f}")
                        with col2:
                            st.metric("Standard Deviation", f"{results['std']:.2f}")
                        with col3:
                            st.metric("Median", f"{results['median']:.2f}")
                        
                except ValueError:
                    st.error("Invalid input. Please enter comma-separated numbers.")
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    
    # Sidebar - System Info
    with st.sidebar:
        st.subheader("💻 System Info")
        device = "GPU" if st.session_state.agent.llm.device == "cuda" else "CPU"
        st.info(f"Running on: {device}")
        
        # Conversation History
        st.subheader("📜 Conversation History")
        history = st.session_state.agent.get_conversation_history()
        
        if len(history) <= 1:  # Only system message
            st.info("No conversations yet.")
        else:
            for msg in history[1:]:  # Skip system message
                with st.expander(f"{msg['role'].title()}: {msg['content'][:50]}..."):
                    st.markdown(msg['content'])
        
        if len(history) > 1 and st.button("Clear History"):
            st.session_state.agent = EnhancedAgent()  # Reinitialize agent
            st.experimental_rerun()

if __name__ == "__main__":
    main() 