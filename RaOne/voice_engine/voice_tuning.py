"""
Module to fine-tune voice output based on dynamic parameters like pitch, speed, volume, and clarity.
Used by the main VoiceController to modulate speech in real-time.
"""

import pyttsx3

class VoiceTuner:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.default_rate = 150
        self.default_volume = 1.0
        self.voices = self.engine.getProperty('voices')

        self.engine.setProperty('voice', self.voices[0].id)

    def set_voice(self, voice_index=0):
        if 0 <= voice_index < len(self.voices):
            self.engine.setProperty('voice', self.voices[voice_index].id)

    def set_volume(self, volume: float):
        """
        Set volume between 0.0 and 1.0
        """
        volume = max(0.0, min(volume, 1.0))
        self.engine.setProperty('volume', volume)

    def set_rate(self, rate: int):
        """
        Set speech rate (words per minute)
        """
        self.engine.setProperty('rate', rate)

    def tune(self, rate=None, volume=None, voice_index=None):
        """
        Apply fine-tuned settings dynamically.
        """
        if rate:
            self.set_rate(rate)
        if volume:
            self.set_volume(volume)
        if voice_index is not None:
            self.set_voice(voice_index)

    def speak_tuned(self, text, rate=None, volume=None, voice_index=None):
        """
        Speak with custom-tuned settings.
        """
        self.tune(rate, volume, voice_index)
        self.engine.say(text)
        self.engine.runAndWait()


if __name__ == "__main__":
    tuner = VoiceTuner()
    tuner.speak_tuned("Welcome to Ra.One voice tuning system!", rate=130, volume=0.9)
