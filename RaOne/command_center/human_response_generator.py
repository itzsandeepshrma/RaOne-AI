import random
from ..brain.sarcasm_recognition import detect_sarcasm

class HumorResponseGenerator:
    def __init__(self):
        self.humor_responses = [
            "Oh, really? I thought you were being serious!",
            "Haha, you got me there!",
            "That was a good one, keep them coming!",
            "I see what you did there. Nice!",
            "Oh, I love sarcasm! More, please!"
        ]
    
    def generate_humor_response(self, user_input):
        """
        Generates a humorous or sarcastic response based on user input.
        """
        if detect_sarcasm(user_input):
            return random.choice(self.humor_responses)
        else:
            return "I don't quite get it, but I'm learning!"
