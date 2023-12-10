def simple_chatbot(user_input):
    # Convert user input to lowercase for easier comparison
    user_input = user_input.lower()

    # Define predefined rules and responses
    greetings = ["hello", "hi", "hey", "hola"]
    farewell = ["bye", "goodbye", "see you"]
    how_are_you = ["how are you", "how are you?", "how are you doing"]

    # Check user input against predefined rules
    if user_input in greetings:
        return "Hello there! How can I help you today?"

    elif user_input in farewell:
        return "Goodbye! Have a great day!"

    elif user_input in how_are_you:
        return "I'm just a simple bot, but thank you for asking!"

    else:
        return "I'm not sure how to respond to that. Can you ask me something else?"

# Example interaction with the chatbot
print("Welcome! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    else:
        response = simple_chatbot(user_input)
        print("Chatbot:", response)
