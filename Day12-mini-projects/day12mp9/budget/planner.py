import math

def set_budget(monthly_income: float, savings_target: float) -> dict:
    needs = monthly_income * 0.5
    wants = monthly_income * 0.3
    savings = monthly_income * 0.2

    if savings < savings_target:
        extra = math.ceil(savings_target - savings)
        savings += extra
        wants -= extra

    return {"Needs": needs, "Wants": wants, "Savings": savings}
