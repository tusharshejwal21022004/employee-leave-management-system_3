# Manager service handles approval workflow

def approve_leave(leave, decision="Approved", comment=""):
    leave.status = decision
    leave.comment = comment
    return leave


def view_pending_requests(all_requests):
    pending = []

    for req in all_requests:
        if req.status == "Pending":
            pending.append(req)

    return pending

def get_team_members():
    return [101, 102, 103]