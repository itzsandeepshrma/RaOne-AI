import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)  # Adjust speed
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()

# Usage: speak("Hello, how can I help you today?")
