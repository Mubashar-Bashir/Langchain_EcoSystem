import streamlit as st
from PIL import Image
from dotenv import load_dotenv
import os
from models.content_generation import ContentGenerationModel
from google.generativeai.types.generation_types import GenerateContentResponse
from models.markdown_format import to_markdown

from google.generativeai import GenerativeModel
import google.generativeai as genai
from models.image_to_text import generate_content_from_image  # Import the 'generate_content_from_image' function


# Load environment variables
load_dotenv()


# Initialize the content generation model
content_generation_model = ContentGenerationModel()
model : GenerativeModel = genai.GenerativeModel("gemini-1.5-flash")

# Set page configuration
st.set_page_config(page_title="GeminiMind", page_icon=":brain:", layout="centered")

# Custom CSS to style the title and background
st.markdown("""
    <style>
        .title {
            color:  #FFFFFF; /* Green color =#2ecc71 */
            font-size: 2em; /* Larger font size */
            font-weight: semi-bold;
            text-align: center;
            
        }
        .background {
            background: url('https://img.freepik.com/premium-photo/purple-background-with-spider-web-red-light_657790-47935.jpg?w=740') no-repeat center center fixed;
            background-size: cover;
        }
        .arrow {
            font-size: 2em;
            color: #FFFFFF;
            text-align: center;
            display: inline;
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
option = st.sidebar.selectbox("Choose a feature", ['Content Generation','Image to Text'] )

# Main Content for content Generation
if option == 'Content Generation':
    st.subheader("Content Generation")
    content_prompt = st.text_area("Enter your content prompt:")
    if st.button("Generate Content"):
        if content_prompt:
            try:
                # Generate content using the Gemini model
                # response = content_generation_model.generate_content(content_prompt, stream=True)
                response : GenerateContentResponse = model.generate_content(content_prompt, stream=True)
                st.write("Generated Content:")

                for chunk in response:
                # text =response.text
                # formatted_markdown=to_markdown(chunk.text)
                    st.write(chunk.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a prompt.")

# Main Content for Image to Text
elif option == 'Image to Text':
    st.title("Image to Text Generator")
# File uploader component
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
    # Load the uploaded image
        image = Image.open(uploaded_file)
        # Display the image
        st.image(image, caption="Uploaded Image")

if st.button("Image to Text"):
    try:
      # Generate content from the image
      generated_content = generate_content_from_image(image)

      # Display the generated content
      st.write("Generated Content:",)
      st.write(generated_content)

    except Exception as e:
      st.error(f"An error occurred: {e}")