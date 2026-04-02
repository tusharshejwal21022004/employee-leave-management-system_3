from services.leave_service import submit_leave_request


def main():
    days = int(input("Enter leave days: "))
    result = submit_leave_request(days)
    print(result)


if __name__ == "__main__":
    main()