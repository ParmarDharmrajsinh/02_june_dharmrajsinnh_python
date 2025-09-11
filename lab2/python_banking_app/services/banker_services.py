# services/banker_services.py

from models.banker import Banker
from models.customer import Customer

class BankerService:

    @staticmethod
    def register():
        print("\n--- Banker Registration ---")
        name = input("Enter your name: ").strip()
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()

        banker = Banker(name, email, password)
        if banker.register():
            print("Banker registered successfully!")
        else:
            print("Registration failed. Email might already exist.")

    @staticmethod
    def login():
        print("\n--- Banker Login ---")
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()

        banker = Banker.login(email, password)
        if banker:
            print(f"Welcome {banker.name}!")
            return True
        else:
            print("Login failed. Invalid credentials.")
            return False

    @staticmethod
    def view_customers():
        print("\n--- All Customers ---")
        customers = Customer.get_all_customers()
        if customers:
            for cust in customers:
                print(f"ID: {cust[0]}, Name: {cust[1]}, Email: {cust[2]}")
        else:
            print("No customers found.")

    @staticmethod
    def update_customer():
        print("\n--- Update Customer ---")
        cust_id = input("Enter Customer ID to update: ").strip()
        name = input("Enter new name: ").strip()
        email = input("Enter new email: ").strip()

        if Customer.update_customer(cust_id, name, email):
            print("Customer updated successfully.")
        else:
            print("Customer update failed. Check ID.")

    @staticmethod
    def delete_customer():
        print("\n--- Delete Customer ---")
        cust_id = input("Enter Customer ID to delete: ").strip()
        confirm = input(f"Are you sure you want to delete customer ID {cust_id}? (Y/N): ").strip().lower()

        if confirm == 'y':
            if Customer.delete_customer(cust_id):
                print("Customer deleted successfully.")
            else:
                print("Deletion failed. Invalid ID.")
        else:
            print("Deletion cancelled.")
