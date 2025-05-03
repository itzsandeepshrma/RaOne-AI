from .speech_to_text import transcribe_voice
from .text_to_speech import speak

def live_conversation():
    while True:
        user_input = transcribe_voice()
        if "exit" in user_input.lower():
            speak("Goodbye.")
            break
        # Connect with AI engine
        response = f"You said: {user_input}"
        speak(response)
