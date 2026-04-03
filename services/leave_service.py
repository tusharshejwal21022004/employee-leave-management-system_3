# Leave service handles leave request submission logic

from models.leave_request import LeaveRequest

leave_cache = {}


def submit_leave_request(employee_id, leave_type, start_date, end_date):
    if employee_id in leave_cache:
        print("Leave fetched from cache")
        return leave_cache[employee_id]

    leave = LeaveRequest(employee_id, leave_type, start_date, end_date)

    leave_cache[employee_id] = leave

    print("Leave request submitted and cached")

    return leave