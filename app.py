# Main application entry point
# Authentication module for employee login

from services.auth_service import login


def authenticate_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    user = login(username, password)
    return user


def main():
    user = authenticate_user()

    if user:
        print("Authenticated successfully")


if __name__ == "__main__":
    main()