class BankAccount:
    def __init__(self, name, acc_number):
        self.name = name
        self.acc_number = acc_number
        self.balance = 0.0

    def __str__(self):
        return f"Account Holder: {self.name}, Account Number: {self.acc_number}, Balance: ₹{self.balance}"

class deposit():
    def deposit(self, amount):
        if amount > 0:

            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

class withdraw():
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")
class BankAccount():
    def __init__(self, name, acc_number):
        self.name = name
        self.acc_number = acc_number
        self.balance = 0.0
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def display(self):
        print("\n--- Account Details ---")
        print(f"Name       : {self.name}")
        print(f"Account No.: {self.acc_number}")
        print(f"Balance    : ₹{self.balance}")

# Main program
class main(BankAccount, deposit, withdraw):
    accounts = {}

    while True:
        print("\n===== Bank Management System =====")
        print("1. Create Account")
        print("2. View Account Details")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        accounts = {}


        if choice == '1':
            name = input("Enter your name: ")
            acc_no = input("Enter new account number: ")
            if acc_no in accounts:
                print("Account already exists!")
            else:
                accounts[acc_no] = BankAccount(name, acc_no)
                print("Account created successfully!")

        elif choice == '2':
            acc_no = input("Enter account number: ")
            if acc_no in accounts:
                accounts[acc_no].display()
            else:
                print("Account not found.")
    
        elif choice == '3':

            acc_no = input("Enter account number: ")
            if acc_no in accounts:
                try:
                    amount = float(input("Enter amount to deposit: "))
                    accounts[acc_no].deposit(amount)
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            else:
                print("Account not found.")
            

        elif choice == '4':
            acc_no = input("Enter account number: ")
            if acc_no in accounts:
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    accounts[acc_no].withdraw(amount)
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            else:
                print("Account not found.")

        elif choice == '5':
            print("Thank you for using the Bank Management System!")
            break

        else:
            print("Invalid choice. Please try again.")
def main(bank_account):
    bank_account = BankAccount("John Doe", "123456789")
    bank_account.deposit(1000)
    bank_account.display()
    bank_account.withdraw(500)
    bank_account.display()
    bank_account.withdraw(600)  # Should show insufficient balance
    bank_account.deposit(-200)   # Should show invalid deposit amount
    bank_account.display()
if __name__ == "__main__":
    main()
# This code defines a simple bank management system with account creation, deposit, and withdrawal functionalities.

