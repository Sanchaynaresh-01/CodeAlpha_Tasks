import nltk
import random
from nltk.chat.util import Chat, reflections

# Download required NLTK data files
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    [
        r'hi|hello|hey',
        ['Hello! How can I assist you today?', 'Hi there! What’s on your mind?', 'Greetings! How can I help?']
    ],
    [
        r'how are you?',
        ['I’m doing well, thank you! How about you?', 'I’m just a chatbot, but I’m happy to chat with you!']
    ],
    [
        r'what is your name?',
        ['I’m a chatbot created to chat with you! You can call me Chatbot.']
    ],
    [
        r'what can you do?',
        ['I can provide information, engage in conversation, or just chat. What do you want to talk about?']
    ],
    [
        r'(.*) your favorite (.*)',
        ['As a chatbot, I don’t have favorites, but I love chatting with you about anything!']
    ],
    [
        r'(.*) help (.*)',
        ['Of course! What do you need help with?', 'I’m here to help! What’s your question?']
    ],
    [
        r'bye|quit|exit',
        ['Goodbye! Have a wonderful day!', 'Take care! Hope to chat again soon!']
    ],
    [
        r'(.*)',
        ['Interesting! Please tell me more.', 'I see, can you elaborate on that?', 'That’s fascinating!']
    ]
]

# Add some personalization to responses based on user input
def respond_to_name(name):
    return f"Nice to meet you, {name}! What else can I do for you?"

def extract_name(user_input):
    # A simple method to extract a name from user input
    tokens = nltk.word_tokenize(user_input)
    for token in tokens:
        if token.istitle() and len(token) > 1:
            return token  # Return the first capitalized word as a name
    return None

# Create a chatbot with the defined pairs
chatbot = Chat(pairs, reflections)

def start_chatbot():
    print("Hi! I'm a simple chatbot. Type 'bye' to exit.")
    user_name = None

    while True:
        user_input = input("You: ")
        
        if 'my name is' in user_input.lower() or 'i am' in user_input.lower():
            # Extract name from user input
            name = extract_name(user_input)
            if name:
                user_name = name
                print(respond_to_name(user_name))
            else:
                print("Chatbot: Nice to meet you! What else can I do for you?")
            continue
        
        if user_name:
            response = chatbot.respond(user_input)
            if response is None:  # If no matching pattern is found
                print("Chatbot: I'm not sure how to respond to that.")
            else:
                print("Chatbot:", response)
        else:
            response = chatbot.respond(user_input)
            if response is None:  
                print("Chatbot: I'm not sure how to respond to that.")
            else:
                print("Chatbot:", response)

        if 'bye' in user_input.lower() or 'quit' in user_input.lower() or 'exit' in user_input.lower():
            break  # Exit the loop to end the chatbot

if name == "main":
    start_chatbot()