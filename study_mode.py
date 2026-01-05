def generate_practice_questions(course_name):
    questions = {
        "Intro to Computer Science": [
            "What is an algorithm?",
            "Explain input and output devices."
        ],
        "Python": [
            "What is a variable in Python?",
            "Difference between list and tuple?"
        ]
    }
    return questions.get(course_name, [])
