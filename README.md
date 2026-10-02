# Rule-Based Chatbot

A simple rule-based chatbot implemented in Python using predefined keywords and intent recognition.

## Overview

This project demonstrates the basic working of a rule-based conversational system.

The chatbot identifies the user's intent by comparing the user's input with predefined keywords and then returns a predefined response for the recognized intent.

The system does not use machine learning or a generative AI model. The responses are based on predefined rules.

## How It Works

The chatbot follows this pipeline:

```text
User Input
    |
    v
Text Preprocessing
    |
    v
Keyword Matching
    |
    v
Intent Recognition
    |
    v
Response Generation
    |
    v
Chatbot Response
```

## Supported Intents

The chatbot currently supports the following intents:

* Greetings
* Python
* Machine Learning
* Artificial Intelligence
* Career

Example keywords include:

```text
hello
hi
hey
python
programming
machine learning
artificial intelligence
internship
career
job
skills
```

## Text Preprocessing

Before intent recognition, the user's input is preprocessed.

The preprocessing performs:

* Conversion to lowercase
* Removal of punctuation
* Removal of unnecessary whitespace

For example:

```text
"What is AI?"
```

is converted to:

```text
"what is ai"
```

## Intent Recognition

The chatbot stores intents and their associated keywords in a Python dictionary.

Example:

```python
intents = {
    "greetings": [
        "hello",
        "hi",
        "hey"
    ],

    "python": [
        "python",
        "programming",
        "coding language"
    ],

    "ml": [
        "ml",
        "machine learning"
    ]
}
```

The user's input is compared with the predefined keywords.

If the input matches a keyword, the corresponding intent is returned.

If no match is found, the chatbot returns:

```text
unknown
```

## Response Generation

Each recognized intent is associated with a predefined response.

For example:

```python
responses = {
    "greetings": "Hi! How can I help you?",

    "python": "Python is a high-level, general-purpose programming language.",

    "ml": "Machine Learning is a subfield of AI..."
}
```

The recognized intent is used to select the appropriate response.

## Example Interaction

```text
Hello World!
Type exit() to Exit...

Enter The Query....
hello

Answer ! ---> Hi! How can I help you?
```

Another example:

```text
Enter The Query....
python

Answer ! ---> Python is a high-level, general-purpose programming language.
```

For an unsupported query:

```text
Enter The Query....
what is blockchain

Answer ! ---> sorry, I can't provide the answer for the given query
```

## Rule-Based Limitation

The chatbot uses keyword-based matching.

For example, if `ai` is defined as a keyword, the chatbot can recognize:

```text
ai
```

However, a longer natural-language query such as:

```text
what is ai
```

may not be recognized by the current matching logic because the complete input does not exactly match the keyword.

This demonstrates an important limitation of simple rule-based systems: they do not understand the meaning or context of a sentence.

More advanced systems can use machine learning, semantic similarity, or large language models to handle different variations of the same query.

## Exit Command

The chatbot can be terminated using:

```text
exit()
```

## Project Files

```text
Chatbot/
│
├── chatbot.py
└── README.md
```

### chatbot.py

Contains the complete implementation of the rule-based chatbot.

## Technologies Used

* Python
* Regular Expressions (`re`)

## Learning Outcomes

This project demonstrates:

* Text preprocessing
* Keyword matching
* Intent recognition
* Dictionary-based rule management
* Regular expressions
* Response mapping
* Fallback handling
* Limitations of rule-based conversational systems

## Conclusion

This project demonstrates how a basic conversational system can be implemented using predefined rules and keyword matching. It provides an introduction to intent recognition while highlighting the limitations of purely rule-based approaches.

## Author

**Syed Kaysan Ul Islam**
B.Tech in Artificial Intelligence & Machine Learning
