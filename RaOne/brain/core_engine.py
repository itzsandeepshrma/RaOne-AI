from .contextual_analysis import analyze_context
from .response_generation import generate_response
from .conversation_flow import update_context
from .emotion_recognition import detect_emotion
from .sarcasm_recognition import detect_sarcasm
from .learning_engine import learn_from_interaction
from .personality_adjustment import adjust_personality

class CoreEngine:
    def __init__(self):
        self.context = {}

    def process_input(self, user_input):
        context_info = analyze_context(user_input, self.context)
        emotion = detect_emotion(user_input)
        sarcasm = detect_sarcasm(user_input)
        personality = adjust_personality(user_input, self.context)
        response = generate_response(user_input, context_info, emotion, sarcasm, personality)
        self.context = update_context(user_input, response, self.context)
        learn_from_interaction(user_input, response)
        return response
