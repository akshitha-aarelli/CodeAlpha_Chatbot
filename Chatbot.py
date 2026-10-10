# CodeAlpha Internship - Task 4: Basic Chatbot


def get_reply(message):
    if message in ("hello", "hi", "hey"):
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "what is your name":
        return "I'm CodeBot, a simple Python chatbot."
    elif message == "help":
        return "Try saying: hello, how are you, what is your name, or bye."
    elif message in ("bye", "goodbye", "exit"):
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I know."


def main():
    print("=== CodeBot ===")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "":
            print("Bot: Please type something.\n")
            continue

        reply = get_reply(user_input)
        print("Bot:", reply, "\n")

        if user_input in ("bye", "goodbye", "exit"):
            break


if __name__ == "__main__":
    main()
