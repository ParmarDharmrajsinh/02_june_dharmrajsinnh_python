# fruit_manager.py

import json

STOCK_FILE = 'fruit_stock.json'

class FruitManager:
    def __init__(self):
        self.stock = self.load_stock()

    def load_stock(self):
        """Load fruit stock from JSON file."""
        try:
            with open(STOCK_FILE, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_stock(self):
        """Save fruit stock to JSON file."""
        with open(STOCK_FILE, 'w') as file:
            json.dump(self.stock, file, indent=4)

    def display_stock(self):
        """Display all fruits in stock."""
        if not self.stock:
            print("\nNo stock available.\n")
        else:
            print("\n--- Fruit Stock ---")
            for fruit, details in self.stock.items():
                print(f"{fruit.title()} - Price: ₹{details['price']} | Qty: {details['quantity']} kg")
            print()

    def add_fruit(self, name, price, quantity):
        """Add or update fruit in stock."""
        name = name.lower()
        if name in self.stock:
            self.stock[name]['quantity'] += quantity
            self.stock[name]['price'] = price
        else:
            self.stock[name] = {'price': price, 'quantity': quantity}
        self.save_stock()

    def update_fruit(self, name, price=None, quantity=None):
        """Update fruit details."""
        name = name.lower()
        if name in self.stock:
            if price is not None:
                self.stock[name]['price'] = price
            if quantity is not None:
                self.stock[name]['quantity'] = quantity
            self.save_stock()
            return True
        return False

    def is_available(self, name, qty):
        """Check if a fruit is available in desired quantity."""
        return name in self.stock and self.stock[name]['quantity'] >= qty

    def deduct_stock(self, name, qty):
        """Deduct fruit stock after purchase."""
        if self.is_available(name, qty):
            self.stock[name]['quantity'] -= qty
            self.save_stock()

    def get_price(self, name):
        """Get price per kg of a fruit."""
        return self.stock[name]['price'] if name in self.stock else 0
