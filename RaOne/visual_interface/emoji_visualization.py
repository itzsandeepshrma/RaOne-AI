def show_emoji(emotion):
    emojis = {
        "happy": "😄",
        "sad": "😢",
        "angry": "😠",
        "neutral": "😐"
    }
    print(f"[Emoji] Detected emotion: {emotion} {emojis.get(emotion, '')}")
