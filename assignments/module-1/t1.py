class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the current balance.")
    def get_balance(self):
        return self.balance
    def __str__(self):
        return f"BankAccount(account_number={self.account_number}, balance={self.balance})"
    def __repr__(self):
        return f"BankAccount({self.account_number}, {self.balance})"
def main():