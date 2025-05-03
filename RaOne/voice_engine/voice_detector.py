import speech_recognition as sr

def detect_wake_word(wake_words=["RaOne", "hey bot"]):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for wake word...")
        audio = recognizer.listen(source)
    try:
        transcript = recognizer.recognize_google(audio).lower()
        print("Heard:", transcript)
        return any(wake in transcript for wake in wake_words)
    except Exception:
        return False
