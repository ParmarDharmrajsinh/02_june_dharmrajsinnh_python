# main.py

from fruit_manager import FruitManager
from customer import Customer
from logger import log_transaction

def input_int(prompt):
    """Safely read a non-negative integer from input."""
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Enter a valid number.")

def display_menu():
    """Display the main menu."""
    print("\n====== Fruit Store Menu ======")
    print("1. View Stock")
    print("2. Buy Fruits")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Add Fruit (Manager)")
    print("6. Update Fruit (Manager)")
    print("7. Exit")

def main():
    manager = FruitManager()
    name = input("Enter your name: ").strip().title()
    user = Customer(name)

    while True:
        display_menu()
        choice = input("Select an option (1-7): ").strip()

        if choice == '1':
            manager.display_stock()

        elif choice == '2':
            fruit = input("Enter fruit name to buy: ").strip().lower()
            qty = input_int("Enter quantity (kg): ")
            if manager.is_available(fruit, qty):
                user.add_to_cart(fruit, qty)
                manager.deduct_stock(fruit, qty)
                log_transaction("purchase", user.name, fruit, qty, manager.get_price(fruit))
                print("Fruit added to cart successfully.")
            else:
                print("Insufficient stock or fruit not available.")

        elif choice == '3':
            user.view_cart()

        elif choice == '4':
            user.view_cart()
            total = user.calculate_total(manager)
            print(f"Total payable: ₹{total}")

        elif choice == '5':
            fruit = input("Enter fruit name to add: ").strip().lower()
            price = input_int("Enter price per kg: ")
            qty = input_int("Enter quantity (kg): ")
            manager.add_fruit(fruit, price, qty)
            log_transaction("stock_add", "Manager", fruit, qty, price)
            print("Fruit stock added successfully.")

        elif choice == '6':
            fruit = input("Enter fruit name to update: ").strip().lower()
            price = input_int("Enter new price (₹): ")
            qty = input_int("Enter new quantity (kg): ")
            if manager.update_fruit(fruit, price, qty):
                log_transaction("stock_update", "Manager", fruit, qty, price)
                print("Fruit updated successfully.")
            else:
                print("Fruit not found in stock.")

        elif choice == '7':
            print("Thank you for using Fruit Store. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
    
