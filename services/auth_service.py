# Authentication service validates employee login credentials

def login(username, password):
    stored_password = "1234"
    if username == "employee" and password == "1234":
        print("Authentication successful")
        return True
        
    return False