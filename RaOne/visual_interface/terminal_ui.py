def start_terminal_ui():
    print("Welcome to RaOne AI Terminal Interface.")
    print("Type your message below or say something...")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("RaOne: Goodbye!")
            break
        print(f"RaOne (simulated): You said '{user_input}'")
