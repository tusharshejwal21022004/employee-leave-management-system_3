# Main application entry point
# Controls authentication, leave submission, approval, and notification flow

from services.auth_service import login
from services.leave_service import submit_leave_request
from services.manager_service import approve_leave, view_pending_requests
from services.notification_service import send_notification
from services.leave_service import leave_cache
from models.employee import Employee


def main():
    """Main workflow for employee dashboard and leave request handling."""

    try:
        username = input("Enter username: ")
        password = input("Enter password: ")

        user = login(username, password)

        if user:
            employee_id = int(input("Enter employee id: "))

            employee = Employee(employee_id, username)
            print("Remaining Leave:", employee.get_remaining_leave())

            leave = submit_leave_request(
                employee_id=employee_id,
                leave_type="Vacation",
                start_date="2026-04-10",
                end_date="2026-04-12"
            )

            pending = view_pending_requests([leave])
            print("Pending Requests:", pending)

            result = approve_leave(leave)

            print("Cached Leave Requests:", leave_cache)
            send_notification(result)

        else:
            print("Login failed")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()