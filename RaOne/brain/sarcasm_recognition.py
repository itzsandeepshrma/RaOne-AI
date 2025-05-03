def detect_sarcasm(text):
    sarcastic_keywords = ["yeah right", "sure", "as if", "totally"]
    return any(kw in text.lower() for kw in sarcastic_keywords)
