# main.py

from services.banker_services import BankerService
from services.customer_services import CustomerService

def display_main_menu():
    print("\n===== Welcome to the Python Banking Application =====")
    print("1. Banker")
    print("2. Customer")
    print("3. Exit")

def display_banker_menu():
    print("\n--- Banker Menu ---")
    print("1. Register")
    print("2. Login")
    print("3. Back to Main Menu")

def display_customer_menu():
    print("\n--- Customer Menu ---")
    print("1. Register")
    print("2. Login")
    print("3. Back to Main Menu")

def main():
    while True:
        display_main_menu()
        choice = input("Select your role (1-3): ").strip()

        if choice == '1':
            while True:
                display_banker_menu()
                banker_choice = input("Enter choice (1-3): ").strip()

                if banker_choice == '1':
                    BankerService.register()
                elif banker_choice == '2':
                    if BankerService.login():
                        while True:
                            print("\n--- Banker Operations ---")
                            print("1. View All Customers")
                            print("2. Update Customer")
                            print("3. Delete Customer")
                            print("4. Logout")

                            op = input("Enter choice: ").strip()
                            if op == '1':
                                BankerService.view_customers()
                            elif op == '2':
                                BankerService.update_customer()
                            elif op == '3':
                                BankerService.delete_customer()
                            elif op == '4':
                                print("Logging out...")
                                break
                            else:
                                print("Invalid option. Try again.")
                    else:
                        print("Invalid login credentials.")
                elif banker_choice == '3':
                    break
                else:
                    print("Invalid input. Try again.")

        elif choice == '2':
            while True:
                display_customer_menu()
                customer_choice = input("Enter choice (1-3): ").strip()

                if customer_choice == '1':
                    CustomerService.register()
                elif customer_choice == '2':
                    customer = CustomerService.login()
                    if customer:
                        while True:
                            print("\n--- Customer Operations ---")
                            print("1. View Balance")
                            print("2. Deposit Amount")
                            print("3. Withdraw Amount")
                            print("4. Logout")

                            op = input("Enter choice: ").strip()
                            if op == '1':
                                customer.view_balance()
                            elif op == '2':
                                customer.deposit()
                            elif op == '3':
                                customer.withdraw()
                            elif op == '4':
                                print("Logging out...")
                                break
                            else:
                                print("Invalid option. Try again.")
                    else:
                        print("Login failed.")
                elif customer_choice == '3':
                    break
                else:
                    print("Invalid input. Try again.")

        elif choice == '3':
            print("Thank you for using the Python Banking Application!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
