from payroll.employee import Employee
from payroll.salary import calculate_gross
from payroll.tax import calculate_tax
from payroll.payslip import generate_payslip

if __name__ == "__main__":
    # Step 1: Create employee
    emp = Employee(101, "Jesy vinoliya", "Software Engineer", "2022-05-10")

    # Step 2: Calculate salary
    basic_salary = 40000
    gross = calculate_gross(basic_salary)
    tax = calculate_tax(gross)
    net = gross - tax

    # Step 3: Generate payslip
    slip = generate_payslip(emp, gross, tax, net)
    print(slip)
