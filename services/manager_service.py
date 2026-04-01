# Manager approval service

def get_pending_leaves():
    return [{"employee_id": 1, "status": "Pending"}]

def approve_leave(leave):
    if leave:
        leave.status = "Approved"
        return leave
    return "Rejected"