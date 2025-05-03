import logging
from .voice_command_processor import process_voice_command
from .user_input_processing import process_text_input
from .multi_modal_command_handler import handle_multi_modal_input

logger = logging.getLogger(__name__)

class CommandProcessor:
    def __init__(self):
        self.context = {}

    def handle_command(self, input_type, input_data):
        """
        Handles command based on input type: 'voice', 'text', or 'multi-modal'
        """
        try:
            if input_type == 'voice':
                return process_voice_command(input_data, self.context)
            elif input_type == 'text':
                return process_text_input(input_data, self.context)
            elif input_type == 'multi-modal':
                return handle_multi_modal_input(input_data, self.context)
            else:
                return "Unsupported input type."
        except Exception as e:
            logger.error(f"CommandProcessor error: {e}")
            return "Oops! I encountered an error while processing your command."
