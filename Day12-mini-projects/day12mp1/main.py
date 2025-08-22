from finance import income, expense, summary

def menu():
    print("\n=== Personal Finance Tracker ===")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. Exit")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Choose option: ")

        if choice == "1":
            amt = float(input("Enter income amount: "))
            src = input("Enter source: ")
            income.add_income(amt, src)
            print("✅ Income added.")
        elif choice == "2":
            amt = float(input("Enter expense amount: "))
            cat = input("Enter category: ")
            expense.add_expense(amt, cat)
            print("✅ Expense added.")
        elif choice == "3":
            report = summary.get_summary()
            print("\n--- Summary ---")
            for k, v in report.items():
                print(f"{k}: {v}")
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice, try again.")
