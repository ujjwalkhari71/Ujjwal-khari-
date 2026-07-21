def get_response(user_input):
    """Return a predefined reply based on user input."""
    user_input = user_input.lower().strip()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    elif user_input == "help":
        return "You can say: hello, how are you, bye"
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can do."


def run_chatbot():
    """Run the chatbot loop until the user says bye."""
    print("Chatbot: Hello! I'm your simple chatbot. Type 'help' for options.")
    print("-" * 50)

    while True:
        user_input = input("You: ")

        if user_input.strip() == "":
            print("Chatbot: Please type something!")
            continue

        response = get_response(user_input)
        print(f"Chatbot: {response}")

        if user_input.lower().strip() == "bye":
            break


# Entry point
run_chatbot()