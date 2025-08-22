from .income import get_total_income
from .expense import get_total_expense

def get_summary():
    income = get_total_income()
    expense = get_total_expense()
    savings = income - expense

    return {
        "Total Income": income,
        "Total Expense": expense,
        "Net Savings": savings
    }
