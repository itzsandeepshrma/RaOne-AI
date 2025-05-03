import speech_recognition as sr
from ..brain.contextual_analysis import analyze_context
from ..brain.response_generation import generate_response

class VoiceCommandProcessor:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen_for_command(self):
        """
        Listens for voice commands from the user.
        """
        with self.microphone as source:
            print("Listening for command...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        return audio

    def process_voice_input(self, audio, context):
        """
        Processes voice input and returns a generated response.
        """
        try:
            text = self.recognizer.recognize_google(audio)
            print(f"User said: {text}")
            normalized = text.strip().lower()
            analyzed_context = analyze_context(normalized, context)
            response = generate_response(normalized, analyzed_context)
            return response
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."
        except sr.RequestError:
            return "Sorry, there's an issue with the speech recognition service."
