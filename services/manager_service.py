# Manager service handles approval workflow

def approve_leave(leave):
    # Approve submitted leave request
    leave.status = "Approved"

    print("Leave approved by manager")

    return leave.status

def check_system_updates():
    """Simulate patch verification."""
    print("System patches verified")