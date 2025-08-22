from school.students import register as student_register, report as student_report
from school.teachers import register as teacher_register, assign as teacher_assign
from school.subjects import register as subject_register, report as subject_report

def menu():
    print("\n=== School Management System ===")
    print("1. Add Student")
    print("2. Add Teacher")
    print("3. Add Subject")
    print("4. Assign Teacher to Subject")
    print("5. List Students")
    print("6. List Subjects")
    print("7. Exit")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Choose option: ")

        if choice == "1":
            sid = input("Enter student ID: ")
            name = input("Enter student name: ")
            grade = input("Enter grade: ")
            student_register.add_student(sid, name, grade)
            print("✅ Student added.")
        elif choice == "2":
            tid = input("Enter teacher ID: ")
            name = input("Enter teacher name: ")
            spec = input("Enter specialization: ")
            teacher_register.add_teacher(tid, name, spec)
            print("✅ Teacher added.")
        elif choice == "3":
            subid = input("Enter subject ID: ")
            name = input("Enter subject name: ")
            subject_register.add_subject(subid, name)
            print("✅ Subject added.")
        elif choice == "4":
            tid = input("Enter teacher ID: ")
            subid = input("Enter subject ID: ")
            teacher_assign.assign_teacher(tid, subid)
            print("✅ Teacher assigned.")
        elif choice == "5":
            print("\n--- Students ---")
            for s in student_report.list_students():
                print(s)
        elif choice == "6":
            print("\n--- Subjects ---")
            for s in subject_report.list_subjects():
                print(s)
        elif choice == "7":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice, try again.")
