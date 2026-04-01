# Main application entry point

from services.auth_service import login
from services.leave_service import submit_leave_request
from services.manager_service import approve_leave, get_pending_leaves
from services.notification_service import send_notification
from functools import lru_cache
import logging


@lru_cache(maxsize=5)
def cached_leave():
    return "cached"


def validate_input(employee_id, leave_type):
    return employee_id > 0 and leave_type != ""


def main():
    username = input("Enter username: ")
    password = input("Enter password: ")

    user = login(username, password)

    if user:
        cached_leave()

        employee_id = int(input("Enter employee id: "))
        leave_type = input("Enter leave type: ")

        if validate_input(employee_id, leave_type):
            pending = get_pending_leaves()
            logging.warning(pending)

            leave = submit_leave_request(
                employee_id,
                leave_type,
                "2026-04-10",
                "2026-04-12"
            )

            result = approve_leave(leave)

            send_notification(result)


if __name__ == "__main__":
    main()