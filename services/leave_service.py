# Leave service handles leave request submission logic

from models.leave_request import LeaveRequest

def get_leave_balance():
    return 10

def submit_leave_request(employee_id, leave_type, start_date, end_date):
    leave_balance = 10

    if leave_balance <= 0:
        return "Insufficient balance"

    return LeaveRequest(employee_id, leave_type, start_date, end_date)


