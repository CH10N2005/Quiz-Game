
questions_database = {
    "fill_in_blank": [
        {"question": "Python uses _____ for comments", "answer": "#", "difficulty": "easy"},
        {"question": "To print in Python we use _____", "answer": "print", "difficulty": "easy"},
        {"question": "HTML stands for HyperText _____ Language", "answer": "Markup", "difficulty": "easy"},
        {"question": "CSS stands for Cascading Style _____", "answer": "Sheets", "difficulty": "easy"},
        {"question": "JavaScript is a _____ programming language", "answer": "interpreted", "difficulty": "medium"},
        {"question": "Variables in Python don't need _____", "answer": "declaration", "difficulty": "medium"},
        {"question": "Python uses _____ for indentation", "answer": "spaces", "difficulty": "easy"},
        {"question": "To get user input in Python use _____", "answer": "input", "difficulty": "easy"},
        {"question": "Python lists are enclosed in _____", "answer": "brackets", "difficulty": "easy"},
        {"question": "To check data type use _____", "answer": "type", "difficulty": "easy"},
        {"question": "Python strings can use _____ quotes", "answer": "single", "difficulty": "easy"},
        {"question": "To convert to integer use _____", "answer": "int", "difficulty": "easy"},
        {"question": "Python functions start with _____", "answer": "def", "difficulty": "easy"},
        {"question": "To import modules use _____", "answer": "import", "difficulty": "easy"},
        {"question": "Python dictionaries use _____ brackets", "answer": "curly", "difficulty": "easy"}
    ],
    "true_false": [
        {"question": "HTML is a programming language", "answer": False, "difficulty": "easy"},
        {"question": "Python is case-sensitive", "answer": True, "difficulty": "easy"},
        {"question": "CSS is used for website styling", "answer": True, "difficulty": "easy"},
        {"question": "JavaScript and Java are the same", "answer": False, "difficulty": "easy"},
        {"question": "Python uses semicolons to end statements", "answer": False, "difficulty": "easy"},
        {"question": "Variables in Python can start with numbers", "answer": False, "difficulty": "medium"},
        {"question": "Python supports multiple inheritance", "answer": True, "difficulty": "medium"},
        {"question": "HTML tags are case-sensitive", "answer": False, "difficulty": "easy"},
        {"question": "CSS can be written inside HTML", "answer": True, "difficulty": "easy"},
        {"question": "Python is an interpreted language", "answer": True, "difficulty": "easy"},
        {"question": "All HTML tags must be closed", "answer": False, "difficulty": "medium"},
        {"question": "Python lists can contain different data types", "answer": True, "difficulty": "easy"},
        {"question": "JavaScript runs only in browsers", "answer": False, "difficulty": "medium"},
        {"question": "Python was created by Guido van Rossum", "answer": True, "difficulty": "easy"},
        {"question": "HTML5 is the latest HTML version", "answer": True, "difficulty": "easy"}
    ]
}

# ALGORITHM: Shuffle and combine questions
def get_shuffled_questions():
    import random
    
   
    all_questions = (
        questions_database["fill_in_blank"] + 
        questions_database["true_false"]
    )
    
    # Shuffle using random.shuffle (Fisher-Yates algorithm)
    random.shuffle(all_questions)
    
    return all_questions

# SIMPLE ACCESS (backward compatible)
fillinblankquestions = [(q["question"], q["answer"]) for q in questions_database["fill_in_blank"]]
TFquestions = [(q["question"], q["answer"]) for q in questions_database["true_false"]]