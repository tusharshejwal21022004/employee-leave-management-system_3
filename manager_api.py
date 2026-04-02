def get_leave_requests_api():
    return {
        "endpoint": "GET /leave-requests/{department_id}",
        "status": "Pending requests fetched"
    }


def approve_leave_api():
    return {
        "endpoint": "PUT /leave-requests/{request_id}/approve",
        "status": "Approved"
    }