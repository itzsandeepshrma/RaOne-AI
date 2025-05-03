class ContextManager:
    def __init__(self):
        self.context = {}
    
    def update_context(self, key, value):
        """
        Updates the conversation context with a new key-value pair.
        """
        self.context[key] = value
    
    def get_context(self, key):
        """
        Retrieves a value from the conversation context based on the key.
        """
        return self.context.get(key, None)
    
    def clear_context(self):
        """
        Clears the entire conversation context.
        """
        self.context.clear()
    
    def manage_conversation(self, user_input):
        """
        Manages the context and flow of the conversation.
        For now, it just demonstrates adding context for a user's query.
        """
        # Example: If the user mentions their name, store it in context
        if "name" in user_input.lower():
            self.update_context("user_name", user_input.split()[-1])
            return f"Got it! I'll remember your name as {user_input.split()[-1]}"
        else:
            return "I'm processing your input, please wait!"
