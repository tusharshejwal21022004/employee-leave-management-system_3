# Manager approval service

def approve_leave(leave):
    """Approve leave request."""
    leave.status = "Approved"
    return leave


def reject_leave(leave):
    """Reject leave request."""
    leave.status = "Rejected"
    return leave


def get_pending_leaves():
    """Return pending leave requests."""
    return [
        {"employee_id": 1, "status": "Pending"},
        {"employee_id": 2, "status": "Pending"}
    ]