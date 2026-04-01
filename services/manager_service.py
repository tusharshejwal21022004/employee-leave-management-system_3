# Manager service handles approval workflow

def approve_leave(leave):
    # Approve submitted leave request
    leave.status = "Approved"

    print("Leave approved by manager")

    return leave.status

def reject_leave(leave):
    leave.status = "Rejected"

def get_pending_leaves(user_id):
    """Return pending leaves."""
    return f"Pending leaves for {user_id}"