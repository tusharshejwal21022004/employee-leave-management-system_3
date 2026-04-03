# Authentication service validates employee login credentials

def login(username, password):
    """Authenticate employee credentials."""

    if not username or not password:
        return False

    if username == "employee" and password == "1234":
        print("Authentication successful")
        return True

    return False