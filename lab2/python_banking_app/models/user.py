# models/user.py

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email.lower().strip()
        self.password = password.strip()
