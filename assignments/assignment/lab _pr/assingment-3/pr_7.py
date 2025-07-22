#7) Write a Python program to handle exceptions in a calculator.

def calculator():
    try:
        print("Simple Calculator")
        num1 = float(input("Enter the first number: "))
        operator = input("Enter the operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2
        else:
            raise ValueError("Invalid operator.")

        print(f"Result: {result}")

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except ZeroDivisionError as zde:
        print(f"Math Error: {zde}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
calculator()
