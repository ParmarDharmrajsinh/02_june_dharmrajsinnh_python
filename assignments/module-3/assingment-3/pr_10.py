#10) Write a Python program to print custom exceptions.

class NegativeNumberError(Exception):
    """Exception raised when a negative number is entered."""
    def __init__(self, value):
        self.value = value
        self.message = f"Invalid input: {value}. Negative numbers are not allowed."
        super().__init__(self.message)
try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError(num)
    else:
        print(f"You entered: {num}")

except NegativeNumberError as e:
    print("\nCustom Exception Caught!")
    print(e)

except ValueError:
    print("\nError: Please enter a valid integer.")

finally:
    print("\nProgram ended gracefully.")
