# Leave request model captures request details submitted by employee

class LeaveRequest:
    def __init__(self, employee_id, leave_type, start_date, end_date):
        self.employee_id = employee_id
        self.leave_type = leave_type
        self.start_date = start_date
        self.end_date = end_date
        self.status = "Pending"   # Initial request status