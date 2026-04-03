# Employee model stores employee basic details and leave balance

employee_cache = {}

class Employee:
    def __init__(self, emp_id, name, leave_balance=20):
        self.emp_id = emp_id
        self.name = name
        self.leave_balance = leave_balance
        employee_cache[self.emp_id] = self

    def calculate_remaining_leave(self, days_taken):
        self.leave_balance -= days_taken
        return self.leave_balance

    def get_remaining_leave(self):
        return self.leave_balance

    def get_team_members():
    return [101, 102, 103]