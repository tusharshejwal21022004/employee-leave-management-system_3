# Manager approval service

def get_pending_leaves():
    return [{"employee_id": 1, "status": "Pending"}]


def approve_leave(leave):
    updated_leave = leave
    updated_leave.status = "Approved"
    return updated_leave