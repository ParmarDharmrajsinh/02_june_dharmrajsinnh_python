#Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input).


def simple_calculator():
    try:
        
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
            result = num1 / num2  
        else:
            print("Invalid operator!")
            return

        
        print(f"Result: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("❌ Invalid input! Please enter numeric values.")
    except ZeroDivisionError:
        print("❌ Error! Cannot divide by zero.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
simple_calculator()
