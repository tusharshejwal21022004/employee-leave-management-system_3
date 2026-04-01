# Main application entry point
# Controls authentication, leave submission, approval, and notification flow

from services.auth_service import login
from services.leave_service import submit_leave_request
from services.manager_service import approve_leave
from services.notification_service import send_notification


employee_id = input("Enter employee id: ")
leave_reason = input("Enter leave reason: ")
start_date = input("Enter start date: ")
end_date = input("Enter end date: ")

def main():
    # Authenticate employee before performing operations
    user = login("employee", "1234")

    if user:
        # Submit leave request with employee details
        leave = submit_leave_request(
            employee_id=1,
            leave_type="Vacation",
            start_date="2026-04-10",
            end_date="2026-04-12"
        )


        # Manager approval simulation
        result = approve_leave(leave)

        # Notify employee about final decision
        send_notification(result)

request_count = 0

def rate_limit():
    global request_count
    request_count += 1
    return request_count <= 5
    
if __name__ == "__main__":
    main()

