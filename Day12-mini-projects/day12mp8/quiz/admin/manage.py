from quiz.questions import load_questions, save_questions

def add_question():
    questions = load_questions()
    q = input("Enter the question: ")
    options = []
    for i in range(4):
        options.append(input(f"Option {i+1}: "))
    ans = input("Correct Answer: ")

    questions.append({
        "question": q,
        "options": options,
        "answer": ans
    })
    save_questions(questions)
    print("✅ Question added successfully!")

def list_questions():
    questions = load_questions()
    for idx, q in enumerate(questions, start=1):
        print(f"{idx}. {q['question']} (Answer: {q['answer']})")
