# Manager service handles approval workflow

def approve_leave(leave):
    # Approve submitted leave request
    leave.status = "Approved"

    print("Leave approved by manager")

    return leave.status


def view_pending_requests(all_requests):
    pending = []

    for req in all_requests:
        if req.status == "Pending":
            pending.append(req)

    return pending