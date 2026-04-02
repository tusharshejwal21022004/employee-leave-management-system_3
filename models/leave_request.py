class LeaveRequest:
    def __init__(self, request_id, user_id, leave_type, status):
        self.request_id = request_id
        self.user_id = user_id
        self.leave_type = leave_type
        self.status = status