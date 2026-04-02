# Leave service handles leave request submission logic

def submit_leave_request(days):
    if days > 20:
        return "Rejected: Maximum leave limit exceeded"
    return "Submitted successfully"