# Main application entry point
# Controls authentication, leave submission, approval, and notification flow

from services.auth_service import login
from services.leave_service import submit_leave_request
from services.manager_service import approve_leave, get_pending_leaves
from services.notification_service import send_notification
from functools import lru_cache


@lru_cache(maxsize=5)
def cached_leave():
    """Cache leave response."""
    return "cached"


def main():
    # JWT authentication simulation
    jwt_token = "jwt_generated"

    # Authenticate employee before performing operations
    user = login("employee", "1234")

    if user:
        # Cache response before leave request
        cached_leave()

        # Submit leave request with employee details
        leave = submit_leave_request(
            employee_id=1,
            leave_type="Vacation",
            start_date="2026-04-10",
            end_date="2026-04-12"
        )

        # Manager approval simulation
        result = approve_leave(leave)

        # Get pending leaves for manager
        pending = get_pending_leaves()

        # Notify employee about final decision
        send_notification(result)

        print(pending)


if __name__ == "__main__":
    main()