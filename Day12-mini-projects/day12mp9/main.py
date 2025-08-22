from budget.planner import set_budget
from budget.tracker import add_expense
from budget.report import monthly_report

def main():
    print("\n=== Budget Planning App ===")
    choice = input("Choose: [1] Set Budget  [2] Add Expense  [3] View Report\n")

    if choice == "1":
        income = float(input("Enter monthly income: "))
        savings_target = float(input("Enter savings target: "))
        budget = set_budget(income, savings_target)
        print("\n💰 Budget Allocation")
        for k, v in budget.items():
            print(f"{k}: {v:.2f}")

    elif choice == "2":
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))
        add_expense(category, amount)

    elif choice == "3":
        monthly_report()

    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()
