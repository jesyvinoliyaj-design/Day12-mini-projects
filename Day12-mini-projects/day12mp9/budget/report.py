from tabulate import tabulate
from datetime import datetime
from collections import defaultdict
from budget.tracker import load_expenses

def monthly_report():
    expenses = load_expenses()
    current_month = datetime.now().strftime("%Y-%m")
    monthly_data = [e for e in expenses if e["date"].startswith(current_month)]

    category_totals = defaultdict(float)
    total_spent = 0

    for e in monthly_data:
        category_totals[e["category"]] += e["amount"]
        total_spent += e["amount"]

    table = [[cat, amt] for cat, amt in category_totals.items()]
    table.append(["TOTAL", total_spent])

    print("\n📊 Monthly Budget Report")
    print(tabulate(table, headers=["Category", "Amount"], tablefmt="pretty"))
