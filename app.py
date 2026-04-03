from services.auth_service import login
from services.leave_service import submit_leave_request, cache_get
from services.manager_service import approve_leave, view_pending_requests, get_team_members
from services.notification_service import send_notification
from models.employee import Employee, cache_employee_get


def manager_put_request(leave):
    decision = input("Approve or Reject: ")
    comment = input("Enter comment: ")

    return approve_leave(leave, decision, comment)


def main():
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")

        user = login(username, password)

        if user:
            employee_id = int(input("Enter employee id: "))

            employee = Employee(employee_id, username)

            cached_employee = cache_employee_get(employee_id)
            print("Cached Employee:", cached_employee)

            print("Remaining Leave:", employee.calculate_remaining_leave(0))

            leave_type = input("Enter leave type: ")
            start_date = input("Enter start date: ")
            end_date = input("Enter end date: ")

            # Cache check before service call
            cached_leave = cache_get(employee_id)

            if cached_leave:
                leave = cached_leave
                print("Leave fetched from cache:", leave)
            else:
                leave = submit_leave_request(
                    employee_id=employee_id,
                    leave_type=leave_type,
                    start_date=start_date,
                    end_date=end_date
                )

            # Manager flow
            team_members = get_team_members()
            all_leaves = []

            for member_id in team_members:
                temp_leave = submit_leave_request(
                    employee_id=member_id,
                    leave_type=leave_type,
                    start_date=start_date,
                    end_date=end_date
                )
                all_leaves.append(temp_leave)

            pending_requests = view_pending_requests(all_leaves)
            print("Manager Pending Requests:", pending_requests)

            # Manager approval (PUT-style)
            leave = manager_put_request(leave)

            if leave.status == "Approved":
                send_notification("Approved")
            else:
                send_notification("Rejected")

        else:
            print("Login failed")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()