import pyttsx3

engine = pyttsx3.init()

def list_voices():
    voices = engine.getProperty('voices')
    print("Available Voices:")
    for index, voice in enumerate(voices):
        print(f"{index}: {voice.name} ({voice.id})")

def set_voice_by_pitch_level(level="normal"):
    voices = engine.getProperty('voices')

    pitch_map = {
        "low": 0,       # Typically deeper voices
        "normal": 1,
        "high": 2       # Typically lighter, higher-pitched voices
    }

    voice_index = pitch_map.get(level.lower(), 1)
    voice_index = min(voice_index, len(voices) - 1)

    engine.setProperty('voice', voices[voice_index].id)
    print(f"[Pitch] Set voice to '{voices[voice_index].name}' for pitch level '{level}'.")

def speak_with_pitch(text, pitch_level="normal"):
    set_voice_by_pitch_level(pitch_level)
    engine.say(text)
    engine.runAndWait()

# Example usage:
# list_voices()
# speak_with_pitch("This is a high-pitched voice.", pitch_level="high")
