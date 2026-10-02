import re

intents = {

    "greetings": [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening",
        "good night"
    ],

    "python": [
        "python",
        "programming",
        "programming language",
        "coding language"
    ],

    "ml": [
        "ml",
        "machine learning"
    ],

    "ai": [
        "ai",
        "artificial intelligence",
        "generative ai"
    ],

    "career": [
        "internship",
        "career",
        "job",
        "skills"
    ]
}


def preprocess_texts(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = " ".join(text.split())
    return text


def recognize_intent(user_input):
    user_input = preprocess_texts(user_input)

    for intent, keywords in intents.items():
        keywords = sorted(keywords , key = len , reverse=True)
        for keyword in keywords:
            pattern = r"\b" + re.escape(keyword) + r"\b"
            if re.search(pattern,user_input):
                return intent

    return "unknown"

# what kind of skills should i have for AIML , and what's the career oppurtunity?

# print(recognize_intent("hola?"))

responses = {
    "greetings": "Hi! How can I help you?",

    "python": "Python is a high-level, general-purpose programming language.",

    "ml": "Machine Learning is a subfield of AI that enables computers to learn patterns from data and make predictions or decisions.",

    "ai": "Artificial Intelligence is a field of computer science focused on creating systems that can perform tasks requiring capabilities such as learning, reasoning, and decision-making.",

    "career": "For an AI/ML career, useful skills include Python, statistics, mathematics, Machine Learning, Deep Learning, and Generative AI."
}

def generate_response(intent):
    if intent == "unknown":
        return "sorry , I cant provide the answer for the given query  , can you please replace the query?"
    
    return responses[intent]



def chatbotfunc():
    print("Hello World!  \n Type exit() to Exit... ")

    while True:
        user_input = input("Enter The Query.... \n ")
        if user_input.lower() == 'exit()':
            print("Have a good day !! Thanks for the Conversation.")
            break
        intent = recognize_intent(user_input)
        resp = generate_response(intent)
        print(f'Answer ! ---> {resp}')




chatbotfunc()