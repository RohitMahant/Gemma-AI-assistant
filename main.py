from utils.gemini_config import GeminiConfig
from utils.audio_config import listen_to_audio, speak_text

if __name__ == "__main__":
    gemini = GeminiConfig()
    print("Chatbot is ready. Say 'exit' to quit.")

    while True:
        user_prompt = listen_to_audio()
        if user_prompt is None:
            continue

        if user_prompt.lower() == "exit":
            print("Goodbye!")
            speak_text("Goodbye!")
            break

        response = gemini.get_response(user_prompt)
        print(f"Bot: {response}")
        speak_text(response)
