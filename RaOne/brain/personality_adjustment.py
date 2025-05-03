def adjust_personality(text, context):
    if "please" in text.lower():
        return "polite"
    return "neutral"
