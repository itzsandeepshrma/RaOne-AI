def store_feedback(user_id, feedback):
    with open("brain/user_feedback_log.txt", "a") as file:
        file.write(f"{user_id}: {feedback}\n")
