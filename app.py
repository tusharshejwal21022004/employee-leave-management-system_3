# Main application entry point
# Controls authentication, leave submission, approval, and notification flow

from services.auth_service import login
from services.leave_service import submit_leave_request, cache_get
from services.manager_service import approve_leave, view_pending_requests, get_team_members
from services.notification_service import send_notification
from models.employee import Employee, cache_employee_get


def main():
    """Main workflow for manager dashboard and leave approval handling."""

    try:
        username = input("Enter username: ")
        password = input("Enter password: ")

        user = login(username, password)

        if user:
            print("Manager Dashboard")

            # Manager fetches team members
            team_members = get_team_members()

            all_leaves = []

            # Generate leave requests for team members
            for member_id in team_members:
                employee = Employee(member_id, f"Employee{member_id}")

                cached_employee = cache_employee_get(member_id)
                print("Cached Employee:", cached_employee)

                leave = submit_leave_request(
                    employee_id=member_id,
                    leave_type="Vacation",
                    start_date="2026-04-10",
                    end_date="2026-04-12"
                )

                cached_leave = cache_get(member_id)
                print("Cached Leave:", cached_leave)

                all_leaves.append(leave)

            # Manager views pending requests
            pending_requests = view_pending_requests(all_leaves)
            print("Manager Pending Requests:", pending_requests)

            # Manager approves/rejects requests
            for leave_request in pending_requests:
                decision = input("Approve or Reject: ")
                comment = input("Enter comment: ")

                leave_request = approve_leave(leave_request, decision, comment)

                send_notification(leave_request.status)

        else:
            print("Login failed")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()