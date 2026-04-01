USER_SCHEMA = {
    "_id": "int",
    "name": "string",
    "email": "string",
    "password_hash": "string",
    "role": "string",
    "remaining_leave_days": "int",
    "leave_history": []
}

def sanitize_input(value):
    return value.replace("<", "").replace(">", "")