import re
from ..brain.contextual_analysis import analyze_context
from ..brain.response_generation import generate_response

def normalize_input(text):
    """
    Cleans and normalizes user text input.
    """
    text = text.strip().lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

def process_text_input(user_input, context):
    """
    Processes text input and returns a generated response.
    """
    normalized = normalize_input(user_input)
    analyzed_context = analyze_context(normalized, context)
    response = generate_response(normalized, analyzed_context)
    return response
