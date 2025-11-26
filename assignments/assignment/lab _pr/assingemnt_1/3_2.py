#: How does the Python code structure work?

# 1. Import statements
import math  # Example import

# 2. Global constants
PI = 3.14159

# 3. Function definitions
def greet_user(name):
    """Greet the user with a welcome message."""
    print(f"Hello, {name}!")

# 4. Class definitions (if needed)
class Circle:
    """A simple class to represent a circle."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return PI * self.radius ** 2

# 5. Main program logic
def main():
    # Example usage
    greet_user("Alice")
    circle = Circle(5)
    print(f"Area of circle: {circle.area()}")

# 6. Entry point check
if __name__ == "__main__":
    main()
