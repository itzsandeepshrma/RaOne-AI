import time
import random

class SmileVisualEffects:
    def __init__(self, ui_renderer):
        """
        ui_renderer: a callable or class that handles visual rendering (e.g., CLI, Web)
        """
        self.ui_renderer = ui_renderer

    def trigger_smile_animation(self):
        """
        Trigger smile-related visual animations (e.g., sparkle, bounce, soft light)
        """
        effect = random.choice(['sparkle', 'light_glow', 'bounce', 'wave_smile'])
        print(f"[SmileEffect] Triggering smile animation: {effect}")
        self.ui_renderer.render_effect(effect)

    def render_smile_reaction(self, confidence_score: float):
        """
        Visualize a smile effect based on how confident the AI is that the user is happy.
        """
        if confidence_score > 0.85:
            self.ui_renderer.render_effect('sparkle')
            self.ui_renderer.render_emoji('😊')
        elif confidence_score > 0.65:
            self.ui_renderer.render_effect('soft_light')
            self.ui_renderer.render_emoji('🙂')
        else:
            print("[SmileEffect] Confidence too low, no animation.")

    def celebrate_user_smile(self):
        """
        Special effect if user smiles or sends positive feedback.
        """
        print("[SmileEffect] User smile detected! Celebrating...")
        self.ui_renderer.render_effect('celebration_confetti')
        time.sleep(1)
        self.ui_renderer.render_text("You made Ra.One smile too!")

class DummyRenderer:
    def render_effect(self, effect):
        print(f"Rendering effect: {effect}")

    def render_emoji(self, emoji):
        print(f"Emoji: {emoji}")

    def render_text(self, text):
        print(f"Text: {text}")

if __name__ == "__main__":
    effects = SmileVisualEffects(DummyRenderer())
    effects.trigger_smile_animation()
    effects.render_smile_reaction(0.9)
    effects.celebrate_user_smile()
