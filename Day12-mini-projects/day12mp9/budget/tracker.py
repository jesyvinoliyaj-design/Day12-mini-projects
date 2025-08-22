import csv
from datetime import datetime
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "expenses.csv")

def add_expense(category: str, amount: float):
    with open(DATA_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().date(), category, amount])
    print("✅ Expense added successfully!")

def load_expenses():
    expenses = []
    with open(DATA_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["amount"] = float(row["amount"])
            expenses.append(row)
    return expenses
