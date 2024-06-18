# Complete script for the quiz

quiz_data = [
    {"question": "What is the capital of France?", "options": ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
     "answer": "A"},
    {"question": "What is 2 + 2?", "options": ["A) 3", "B) 4", "C) 5", "D) 6"], "answer": "B"},
    {"question": "Who wrote 'Hamlet'?",
     "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Jane Austen"], "answer": "B"},
    # Add more questions here to reach 100 questions
    # ...
]


def ask_question(question_data, question_number):
    print(f"Question {question_number + 1}: {question_data['question']}")
    for option in question_data['options']:
        print(option)
    answer = input("Your answer (A, B, C, or D): ").strip().upper()
    while answer not in ["A", "B", "C", "D"]:
        print("Invalid input. Please enter A, B, C, or D.")
        answer = input("Your answer (A, B, C, or D): ").strip().upper()
    return answer


def run_quiz(quiz_data):
    user_answers = []
    correct_count = 0

    for i, question_data in enumerate(quiz_data):
        user_answer = ask_question(question_data, i)
        correct = user_answer == question_data['answer']
        user_answers.append((i, user_answer, correct))
        if correct:
            correct_count += 1

    print("\nQuiz Completed!")
    print(f"You answered {correct_count} out of {len(quiz_data)} questions correctly.")

    return user_answers


def review_answers(quiz_data, user_answers):
    print("\nReview your answers:")
    for i, user_answer, correct in user_answers:
        question_data = quiz_data[i]
        print(f"Question {i + 1}: {question_data['question']}")
        print(f"Your answer: {user_answer} {'(Correct)' if correct else '(Incorrect)'}")
        print(f"Correct answer: {question_data['answer']}")
        print()


# To run the quiz
user_answers = run_quiz(quiz_data)
review_answers(quiz_data, user_answers)

