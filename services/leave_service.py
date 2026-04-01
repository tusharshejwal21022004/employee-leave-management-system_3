# Leave service handles leave request submission logic

from models.leave_request import LeaveRequest


def submit_leave_request(employee_id, leave_type, start_date, end_date):
    # Create leave request object
    leave = LeaveRequest(employee_id, leave_type, start_date, end_date)

    print("Leave request submitted")

    return leave

leave_cache = {}

def optimize_leave_response():
    leave_cache["latest"] = "Leave cached"