from quiz.admin.manage import add_question, list_questions
from quiz.user.play import start_quiz

def main():
    print("\n=== Online Quiz Application ===")
    mode = input("Choose mode: [1] Admin  [2] User\n")

    if mode == "1":
        action = input("Admin Options: [1] Add Question  [2] List Questions\n")
        if action == "1":
            add_question()
        elif action == "2":
            list_questions()
        else:
            print("Invalid choice.")
    elif mode == "2":
        start_quiz()
    else:
        print("Invalid mode.")

if __name__ == "__main__":
    main()
