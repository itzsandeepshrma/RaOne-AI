from terminal_ui import run_terminal_ui
from web_interface import run_web_interface

def main():
    choice = input("Choose interface [1] Terminal UI or [2] Web UI: ").strip()
    if choice == "1":
        run_terminal_ui()
    elif choice == "2":
        run_web_interface()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
