# Employee model stores employee basic details and leave balance

class Employee:
    def __init__(self, emp_id, name, leave_balance):
        self.emp_id = emp_id
        self.name = name
        self.leave_balance = leave_balance
        self.history = []   # Stores approved leave history