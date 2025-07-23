# 2. models/base_user.py

class BaseUser:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email.lower().strip()
        self.password = password.strip()

    def validate_email(self):
        return "@" in self.email and "." in self.email
