questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"],
        "answer": "A",
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. Java", "C. HTML", "D. C++"],
        "answer": "C",
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Process Unit",
            "B. Computer Personal Unit",
            "C. Central Processing Unit",
            "D. Control Panel Unit",
        ],
        "answer": "C",
    },
]

score = 0
total = len(questions)

print("---- Python Quiz ----")
print("Choose the correct option (A/B/C/D)")
print("----")

for i, q in enumerate(questions, 1):
    print(f"\nQ{i}. {q['question']}")
    for option in q['options']:
        print(option)

    user_ans = input("Enter your answer: ").upper()

    if user_ans == q['answer']:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! Correct answer is {q['answer']}\n")

print("---- Quiz Completed ----")
print(f"Your Score: {score} out of {total}")