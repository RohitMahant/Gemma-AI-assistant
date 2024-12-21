import speech_recognition as sr
import pyttsx3

def listen_to_audio():
    """
    Captures audio from the microphone and converts it to text.
    Returns the recognized text or None if an error occurs.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Speak now!")
        try:
            audio = recognizer.listen(source)
            user_input = recognizer.recognize_google(audio)
            print(f"You said: {user_input}")
            return user_input
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            print(f"Speech recognition error: {e}")
        return None

def speak_text(text):
    """
    Converts the given text to speech and plays it.
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
