from leave_api import submit_leave_request_api
from manager_api import get_leave_requests_api, approve_leave_api


def main():
    print(submit_leave_request_api())
    print(get_leave_requests_api())
    print(approve_leave_api())


if __name__ == "__main__":
    main()