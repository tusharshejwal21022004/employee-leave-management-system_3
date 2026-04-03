# Manager service handles approval workflow

approval_cache = {}


def approve_leave(leave, decision="Approved", comment=""):
    leave.status = decision
    leave.comment = comment

    approval_cache[leave.employee_id] = leave.status

    return leave


def view_pending_requests(all_requests):
    return [req for req in all_requests if req.status == "Pending"]


def get_team_members():
    return [101, 102, 103]