# task1_chatbot.py
# Rule-Based Chatbot for CodSoft Internship

def chatbot():
    print("Welcome to CodBot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ").lower()

        if 'hello' in user_input or 'hi' in user_input:
            print("CodBot: Hello! How can I assist you today?")
        elif 'your name' in user_input:
            print("CodBot: I am CodBot, your friendly chatbot!")
        elif 'internship' in user_input:
            print("CodBot: This chatbot is built as part of the CodSoft AI Internship.")
        elif 'bye' in user_input or 'exit' in user_input:
            print("CodBot: Goodbye! Have a great day.")
            break
        else:
            print("CodBot: I'm not sure how to respond to that. Can you rephrase?")

if __name__ == "__main__":
    chatbot()
