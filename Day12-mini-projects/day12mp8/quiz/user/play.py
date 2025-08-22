import random
import time
from quiz.questions import load_questions
from quiz.evaluate import check_answer
from quiz.score import display_score

def start_quiz():
    questions = load_questions()
    random.shuffle(questions)
    results = []

    print("\n🎯 Welcome to the Quiz!\n")

    for q in questions:
        print(q["question"])
        for i, opt in enumerate(q["options"], start=1):
            print(f"{i}. {opt}")
        ans = input("Your answer: ")

        try:
            selected = q["options"][int(ans) - 1]
        except:
            selected = ans  # user typed text directly

        correct = check_answer(selected, q["answer"])
        results.append(correct)

        print("✅ Correct!\n" if correct else f"❌ Wrong! Correct answer: {q['answer']}\n")
        time.sleep(1)

    display_score(results)
