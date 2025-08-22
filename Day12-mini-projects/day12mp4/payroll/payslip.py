from datetime import datetime

def generate_payslip(employee, gross, tax, net):
    slip = f"""
    =========================
           PAYSLIP
    =========================
    Employee: {employee.name}
    Role: {employee.role}
    Employee ID: {employee.emp_id}
    Date: {datetime.now().strftime("%Y-%m-%d")}
    -------------------------
    Gross Salary: {gross}
    Tax Deducted: {tax}
    Net Salary:   {net}
    =========================
    """
    return slip
