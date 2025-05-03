import pyttsx3
import random

engine = pyttsx3.init()

def configure_sarcastic_voice():
    voices = engine.getProperty('voices')
    if len(voices) > 2:
        engine.setProperty('voice', voices[2].id)
    else:
        engine.setProperty('voice', voices[0].id)

    rate = random.randint(120, 140)
    engine.setProperty('rate', rate)

    volume = random.uniform(0.85, 1.0)
    engine.setProperty('volume', volume)

    print(f"[Sarcasm] Voice configured with rate={rate}, volume={round(volume, 2)}")

def speak_sarcastically(text):
    configure_sarcastic_voice()
    mock_text = generate_mocking_case(text)
    engine.say(mock_text)
    engine.runAndWait()

def generate_mocking_case(text):
    result = ''
    toggle = True
    for c in text:
        if c.isalpha():
            result += c.upper() if toggle else c.lower()
            toggle = not toggle
        else:
            result += c
    return result

# Example:
# speak_sarcastically("Oh really? That was soooo smart.")
