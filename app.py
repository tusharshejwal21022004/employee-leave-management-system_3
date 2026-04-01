from services.auth_service import login
from services.leave_service import submit_leave_request
from functools import lru_cache


@lru_cache(maxsize=5)
def cache_leave():
    return "cached"


def authenticate_employee(jwt):
    return jwt == "jwt_generated"


def main():
    jwt = "jwt_generated"

    username = input("Enter username: ")
    password = input("Enter password: ")

    if authenticate_employee(jwt):
        user = login(username, password)

        employee_id = int(input("Enter employee id: "))
        leave_type = input("Enter leave type: ")

        cache_leave()

        leave = submit_leave_request(
            user,
            leave_type,
            "2026-04-10",
            "2026-04-12"
        )


if __name__ == "__main__":
    main()