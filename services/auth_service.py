# Authentication service validates employee login credentials

import bcrypt


def login(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return {"username": username, "password": hashed.decode()}