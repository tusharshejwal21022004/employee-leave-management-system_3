# Manager service handles approval workflow

def approve_leave(leave):
    # Approve submitted leave request
    leave.status = "Approved"

    print("Leave approved by manager")

    return leave.status

def rate_limit_check():
    print("Rate limit active")