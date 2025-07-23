# 3. models/banker.py

from .base_user import BaseUser

class Banker(BaseUser):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
