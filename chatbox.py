# ------------------------------------------------------
# Copyright (c) 2026 Antonis Koukoumelas. All rights reserved.
# Αυτό το project δημιουργήθηκε από Antonis Koukoumelas.
# ------------------------------------------------------

# chatbot.py

responses = {
    "hello": "Hi there! How can I help you?",
    "python": "Python is a programming language.",
    "name": "I am your simple chatbot.",
    "bye": "Goodbye! See you later."
}

def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        msg = input("You: ").lower()
        if msg == "bye":
            print("Chatbot: Goodbye!")
            break
        answer = responses.get(msg, "I don't understand.")
        print("Chatbot:", answer)

if __name__ == "__main__":
    chat()
