import math

def calculate_tax(gross_salary):
    if gross_salary <= 25000:
        return 0
    elif gross_salary <= 50000:
        return math.ceil(gross_salary * 0.1)
    else:
        return math.ceil(gross_salary * 0.2)
