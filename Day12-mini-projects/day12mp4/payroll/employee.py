from datetime import datetime

class Employee:
    def __init__(self, emp_id, name, role, join_date):
        self.emp_id = emp_id
        self.name = name
        self.role = role
        self.join_date = datetime.strptime(join_date, "%Y-%m-%d")

    def __str__(self):
        return f"{self.emp_id} - {self.name} ({self.role})"
