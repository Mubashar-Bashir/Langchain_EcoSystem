import os
from dotenv import load_dotenv
import google.generativeai as genai
from google.generativeai.types.generation_types import GenerateContentResponse

# Load environment variables from .env file
load_dotenv()

class ContentGenerationModel:
    def __init__(self):
        self.api_key = os.getenv('GEMINI_SECRET_KEY')
        if not self.api_key:
            raise ValueError("API key not found in environment variables.")
        
        # Configure the GenerativeModel with the API key
        genai.configure(api_key=self.api_key)

        # Initialize the GenerativeModel
        self.model = genai.GenerativeModel()  # Ensure this is the correct class per the library's documentation

    def generate_content(self, prompt):
        try:
            # Use the GenerativeModel to generate content
            response = self.model.generate_content(prompt)  # This method must match the library's API
            return response  # Adjust this to match the actual response object structure
        except Exception as e:
            raise RuntimeError(f"An error occurred during content generation: {e}")

    
