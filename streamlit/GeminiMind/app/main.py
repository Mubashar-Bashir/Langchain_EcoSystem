import streamlit as st
from dotenv import load_dotenv
import os
from models.content_generation import ContentGenerationModel

# Load environment variables
load_dotenv()

# Initialize the content generation model
content_generation_model = ContentGenerationModel()

# Set page configuration
st.set_page_config(page_title="GeminiMind", page_icon=":brain:", layout="centered")

# Custom CSS to style the title and background
st.markdown("""
    <style>
        .title {
            color: #2ecc71; /* Green color */
            font-size: 2.5em; /* Larger font size */
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }
        .background {
            background: url('https://www.example.com/your-background-image.jpg') no-repeat center center fixed;
            background-size: cover;
        }
        .arrow {
            font-size: 3em;
            color: #2ecc71;
            text-align: center;
            display: block;
            margin: 20px 0;
        }
        .subheader {
            font-size: 1em; /* Adjust the size here */
            color: lightgray; /* Light gray color */
            text-align: center;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# HTML for title and arrow background
st.markdown("""
    <div class="background">
        <div class="title">GeminiMind Prototype</div>
        <div class="arrow">➤</div>
        <div class="subheader">Prepared By Mubashar Bhatti GenAI-Builders</div>
    </div>
""", unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Features")
option = st.sidebar.selectbox("Choose a feature", ['Content Generation'])

# Main Content
if option == 'Content Generation':
    st.subheader("Content Generation")
    content_prompt = st.text_area("Enter your content prompt:")
    if st.button("Generate Content"):
        if content_prompt:
            try:
                # Generate content using the Gemini model
                response = content_generation_model.generate_content("what is life?")
                st.write("Generated Content:")
                st.write(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a prompt.")
