# Main application entry point
# Controls authentication, leave submission, approval, and notification flow

from services.auth_service import login
from services.leave_service import submit_leave_request
from services.manager_service import approve_leave
from services.notification_service import send_notification

jwt_token = "jwt_generated"

username = input("Enter username: ")
password = input("Enter password: ")

user = login(username, password)

def main():
   
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


if __name__ == "__main__":
    main()