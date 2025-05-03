import pyttsx3
from voice_engine.pitch_control import PitchController
from voice_engine.speed_control import SpeedController
from voice_engine.smile_voice_filter import SmileVoiceFilter
from voice_engine.sarcastic_voice_filter import SarcasticVoiceFilter

class VoiceController:
    def __init__(self):
        """
        Initializes the text-to-speech engine and voice modifiers.
        """
        self.engine = pyttsx3.init()
        self.pitch_controller = PitchController()
        self.speed_controller = SpeedController()
        self.smile_filter = SmileVoiceFilter()
        self.sarcastic_filter = SarcasticVoiceFilter()

        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1.0)

    def configure_voice(self, emotion="neutral"):
        """
        Adjusts pitch, speed, and effects based on emotion.
        """
        pitch = self.pitch_controller.get_pitch(emotion)
        speed = self.speed_controller.get_speed()

        self.engine.setProperty('rate', int(150 * speed))

        print(f"[VoiceController] Emotion: {emotion}, Pitch: {pitch}, Speed: {speed}")

      
        if emotion == "happy":
            self.smile_filter.apply()
        elif emotion == "sarcastic":
            self.sarcastic_filter.apply()

    def speak(self, text, emotion="neutral"):
        """
        Speaks the given text with emotional adjustments.
        """
        self.configure_voice(emotion)
        print(f"[VoiceController] Speaking: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

# Example usage
if __name__ == "__main__":
    vc = VoiceController()
    vc.speak("Hello, I am Ra.One, your AI companion!", emotion="happy")
