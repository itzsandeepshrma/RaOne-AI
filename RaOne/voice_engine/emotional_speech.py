import pyttsx3

engine = pyttsx3.init()
engine.setProperty('volume', 1.0)

# Voice properties based on emotion
EMOTION_SETTINGS = {
    "neutral": {"rate": 175, "pitch": 50},
    "happy": {"rate": 190, "pitch": 70},
    "sad": {"rate": 120, "pitch": 40},
    "angry": {"rate": 200, "pitch": 80},
    "excited": {"rate": 210, "pitch": 85},
    "calm": {"rate": 150, "pitch": 45},
}

def set_emotion(emotion="neutral"):
    settings = EMOTION_SETTINGS.get(emotion.lower(), EMOTION_SETTINGS["neutral"])
    engine.setProperty('rate', settings["rate"])
    # Pitch control isn't native in pyttsx3, depends on voice; we simulate with rate and tone
    print(f"[Emotion] Speaking with '{emotion}' tone (rate: {settings['rate']})")

def speak_emotionally(text, emotion="neutral"):
    set_emotion(emotion)
    engine.say(text)
    engine.runAndWait()

# Example usage:
# speak_emotionally("Hello, I'm happy to talk to you!", emotion="happy")
