from taskmanager import add_task, update_task, delete_task, list_tasks, set_priority, show_calendar

def main():
    print("\n=== Task Management System ===")
    choice = input("Choose: [1] Add [2] Update [3] Delete [4] List [5] Set Priority [6] Calendar\n")

    if choice == "1":
        title = input("Enter task title: ")
        due = input("Enter due date (YYYY-MM-DD): ")
        priority = input("Enter priority (Low/Medium/High): ")
        add_task(title, due, priority)

    elif choice == "2":
        task_id = int(input("Enter task ID: "))
        field = input("Enter field to update (title/due/status): ")
        value = input("Enter new value: ")
        update_task(task_id, **{field: value})

    elif choice == "3":
        task_id = int(input("Enter task ID to delete: "))
        delete_task(task_id)

    elif choice == "4":
        list_tasks()

    elif choice == "5":
        task_id = int(input("Enter task ID: "))
        priority = input("Enter new priority (Low/Medium/High): ")
        set_priority(task_id, priority)

    elif choice == "6":
        show_calendar()

    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()
