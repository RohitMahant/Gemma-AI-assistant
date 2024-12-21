import os
from dotenv import load_dotenv
import google.generativeai as genai

class GeminiConfig:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("API key is not set. Please check your .env file or environment variables.")
        
        genai.configure(api_key=api_key)

        # Create the model
        self.generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }

        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=self.generation_config,
        )

    def get_response(self, prompt: str):
        try:
            chat_session = self.model.start_chat(
                history=[
                    {
                        "role": "user",
                        "parts": ["hey\n"],
                    },
                    {
                        "role": "model",
                        "parts": ["Hey there! What can I do for you today? \n"],
                    },
                ]
            )

            response = chat_session.send_message(prompt)
            return response.text

        except Exception as err:
            return f"Error: {str(err)}"


