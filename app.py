from services.auth_service import login
from services.leave_service import submit_leave_request
from services.notification_service import send_notification
from functools import lru_cache


@lru_cache(maxsize=5)
def cache_user():
    return "cached"


def authenticate_employee(jwt):
    return jwt == "jwt_generated"


def main():
    jwt = "jwt_generated"

    user_username = input("Enter your username: ")
    user_password = input("Enter your password: ")

    if authenticate_employee(jwt):
        user = login(user_username, user_password)

        employee_id = int(input("Enter employee id: "))
        leave_type = input("Enter leave type: ")

        cache_user()

        leave = submit_leave_request(
            user,
            leave_type,
            "2026-04-10",
            "2026-04-12"
        )

        email_service = "EmailJS"

        send_notification(leave)


if __name__ == "__main__":
    main()