from models.banker import Banker
from models.customer import Customer
from services.banker_service import BankerService
from services.customer_service import CustomerService

def main_menu():
    while True:
        print("\n📌 Welcome to Python Bank")
        print("1. Banker Login")
        print("2. Customer Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            banker_menu()
        elif choice == "2":
            customer_menu()
        elif choice == "3":
            print("👋 Exiting... Have a great day!")
            break
        else:
            print("❌ Invalid choice. Try again.")

def banker_menu():
    print("\n📋 Banker Options")
    email = input("Enter email: ")
    password = input("Enter password: ")
    banker = BankerService.login_banker(email, password)
    if banker:
        while True:
            print("\n1. View All Customers\n2. Delete Customer\n3. Back to Main")
            choice = input("Choice: ")
            if choice == "1":
                for c in BankerService.view_customers():
                    print(c)
            elif choice == "2":
                cid = input("Enter Customer ID to delete: ")
                confirm = input("Are you sure? (Y/N): ")
                if confirm.lower() == "y":
                    BankerService.delete_customer(cid)
            elif choice == "3":
                break
            else:
                print("❌ Invalid input")
    else:
        print("❌ Invalid Banker Credentials")

def customer_menu():
    print("\n👤 Customer Options")
    email = input("Email: ")
    password = input("Password: ")
    user = CustomerService.login_customer(email, password)
    if user:
        customer_id = user[0]
        while True:
            print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Back")
            choice = input("Choice: ")
            if choice == "1":
                amt = float(input("Enter amount to deposit: "))
                CustomerService.update_balance(customer_id, amt, "deposit")
                print("✅ Deposit successful.")
            elif choice == "2":
                amt = float(input("Enter amount to withdraw: "))
                if amt <= CustomerService.get_balance(customer_id):
                    CustomerService.update_balance(customer_id, amt, "withdraw")
                    print("✅ Withdraw successful.")
                else:
                    print("❌ Insufficient balance.")
            elif choice == "3":
                bal = CustomerService.get_balance(customer_id)
                print(f"💰 Your balance: ₹{bal}")
            elif choice == "4":
                break
            else:
                print("❌ Invalid input")
    else:
        print("❌ Customer not found!")

if __name__ == "__main__":
    main_menu()
