class SpeedController:
    def __init__(self, default_speed=1.0):
        """
        Initializes the speed controller with a default playback speed.
        """
        self.playback_speed = default_speed 

    def set_speed(self, speed: float):
        """
        Sets the playback speed for speech output.
        speed: float - 0.5 (slow) to 2.0 (fast)
        """
        if 0.5 <= speed <= 2.0:
            print(f"[SpeedControl] Setting playback speed to {speed}x")
            self.playback_speed = speed
        else:
            raise ValueError("[SpeedControl] Speed must be between 0.5x and 2.0x")

    def get_speed(self) -> float:
        """
        Returns the current playback speed.
        """
        return self.playback_speed

    def apply_to_audio(self, audio_data):
        """
        Placeholder method to apply speed control to audio data.
        In a real implementation, this would modify the audio playback speed.
        """
        print(f"[SpeedControl] Applying speed {self.playback_speed}x to audio")
        return audio_data 
      
