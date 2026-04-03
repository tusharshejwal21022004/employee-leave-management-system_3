# Main application entry point
# Controls authentication, leave submission, approval, and notification flow

from services.auth_service import login
from services.leave_service import submit_leave_request, leave_cache
from services.manager_service import approve_leave, view_pending_requests, get_team_members
from services.notification_service import send_notification
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

            leave_type = input("Enter leave type: ")
            start_date = input("Enter start date: ")
            end_date = input("Enter end date: ")

            leave = submit_leave_request(
                employee_id=employee_id,
                leave_type=leave_type,
                start_date=start_date,
                end_date=end_date
            )

            # Cache retrieval
            cached_leave = leave_cache.get(employee_id)
            print("Cached Leave:", cached_leave)

            cached_again = submit_leave_request(
                employee_id=employee_id,
                leave_type=leave_type,
                start_date=start_date,
                end_date=end_date
            )

            print("Second fetch from cache:", cached_again)

            # Manager pending requests
            pending_requests = view_pending_requests([leave])
            print("Manager Pending Requests:", pending_requests)

            # Approval / rejection with comment
            decision = input("Approve or Reject: ")
            comment = input("Enter comment: ")

            leave = approve_leave(leave, decision, comment)

            remaining = employee.calculate_remaining_leave(2)
            print("Updated Remaining Leave:", remaining)

            # Notification
            send_notification(leave.status)

        else:
            print("Login failed")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()