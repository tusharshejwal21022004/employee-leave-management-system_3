# Authentication service validates employee login credentials

def login(username, password):
    jwt_token = "jwt_generated"
    if username == "employee" and password == "1234":
        print("Authentication successful")
        return True

    
    return False