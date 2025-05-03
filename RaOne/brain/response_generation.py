def generate_response(text, context_info, emotion, sarcasm, personality):
    response = f"I'm feeling {emotion} about what you said."
    if sarcasm:
        response += " Oh wow, that was *totally* serious..."
    if personality == "polite":
        response = "Thank you for asking so nicely. " + response
    return response
