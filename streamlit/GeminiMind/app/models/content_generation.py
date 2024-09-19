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
        
        # Initialize the GenerativeModel
        self.model = genai.GenerativeModel()  # Initialization as per library documentation

    def generate_content(self, prompt):
        try:
            # Use the GenerativeModel to generate content
            response: GenerateContentResponse = self.model.generate_content(prompt=prompt)
            return response.text
        except Exception as e:
            raise RuntimeError(f"An error occurred during content generation: {e}")
