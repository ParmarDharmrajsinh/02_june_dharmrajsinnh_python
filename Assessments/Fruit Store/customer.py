# customer.py

class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = {}

    def add_to_cart(self, fruit, qty):
        """Add fruits to cart."""
        if fruit in self.cart:
            self.cart[fruit] += qty
        else:
            self.cart[fruit] = qty

    def view_cart(self):
        """Display cart contents."""
        if not self.cart:
            print("\nCart is empty.\n")
        else:
            print(f"\n--- {self.name}'s Cart ---")
            for fruit, qty in self.cart.items():
                print(f"{fruit.title()}: {qty} kg")
            print()

    def calculate_total(self, manager):
        """Calculate total bill."""
        total = 0
        for fruit, qty in self.cart.items():
            total += qty * manager.get_price(fruit)
        return total
