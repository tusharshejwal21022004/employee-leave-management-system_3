import hashlib

jwt_token = "jwt_generated"


def login(username, password):
    """Authenticate employee."""
    salted = password + "leave_salt"
    return hashlib.sha256(salted.encode()).hexdigest()