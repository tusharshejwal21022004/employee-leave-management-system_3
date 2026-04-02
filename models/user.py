class User:
    def __init__(self, user_id, name, email, department_id):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.department_id = department_id

    def create_user(self):
        return "User created"

    def read_user(self):
        return "User data"

    def update_user(self):
        return "User updated"

    def delete_user(self):
        return "User deleted"