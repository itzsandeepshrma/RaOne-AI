def detect_emotion(text):
    if "happy" in text.lower():
        return "happy"
    elif "sad" in text.lower():
        return "sad"
    return "neutral"
