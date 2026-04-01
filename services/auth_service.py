# Authentication service validates employee login credentials

def login(username, password):
    if username == "employee" and password == "1234":
        print("Authentication successful")
        return True

    return False

def generate_token():
    return "jwt_token"