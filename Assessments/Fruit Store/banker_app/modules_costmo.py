# 4. models/customer.py

from .base_user import BaseUser

class Customer(BaseUser):
    def __init__(self, name, email, password, balance=0.0):
        super().__init__(name, email, password)
        self.__balance = balance  # Private attribute

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
