import time
from cinematic_boot.animation_effects import play_animation_sequence
from cinematic_boot.intro_visuals import display_intro_visuals
import playsound
import os

def play_intro_audio():
    audio_path = os.path.join(os.path.dirname(__file__), "audio_intro.mp3")
    try:
        playsound.playsound(audio_path)
    except Exception as e:
        print(f"[Audio Error] Could not play intro audio: {e}")

def initiate_boot_sequence():
    print("Initializing RaOne AI System...")
    time.sleep(1)
    play_animation_sequence()
    display_intro_visuals()
    play_intro_audio()
    print("RaOne AI is now online and ready to assist you.")

if __name__ == "__main__":
    initiate_boot_sequence()
