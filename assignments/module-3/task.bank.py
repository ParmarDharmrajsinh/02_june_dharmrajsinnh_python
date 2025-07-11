class bankaccount:
    def __init__(self,name ,acc_number,blance=0):
        self.name=name
        self.acc_number=acc_number
        self.blance=blance


    def deposit(self, amount):
        if amount > 2000:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")
            
    def display(self):
        print("\n--- Account Details ---")
        print(f"Name       : {self.name}")
        print(f"Account No.: {self.acc_no}")
        print(f"Balance    : ₹{self.balance}")
    def main():
        accounts = {}

    while True:
        print("\n===== Bank Management System =====")
        print("1. Create Account")
        print("2. View Account Details")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        
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
                amount = float(input("Enter amount to deposit: "))
                accounts[acc_no].deposit(amount)
            else:
                print("Account not found.")

        elif choice == '4':
            acc_no = input("Enter account number: ")
            if acc_no in accounts:
                amount = float(input("Enter amount to withdraw: "))
                accounts[acc_no].withdraw(amount)
            else:
                print("Account not found.")

        elif choice == '5':
            print("Thank you for using the Bank Management System!")
            break

        else:
             print("Invalid choice. Please try again.")



