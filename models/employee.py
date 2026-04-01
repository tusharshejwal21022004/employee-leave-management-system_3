class Employee:
    def __init__(self):
        self.mongo_collection = "employees"
        self.email = "employee@test.com"

    def create_employee(self):
        return "saved"

    def read_employee(self):
        return "employee data"