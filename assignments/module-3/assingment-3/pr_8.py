# 8) Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).

def handle_multiple_exceptions():
    try:
        filename = input("Enter filename to open: ")
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile content:")
            print(content)
        numerator = int(input("\nEnter numerator: "))
        denominator = int(input("Enter denominator: "))
        result = numerator / denominator
        print(f"Result of division: {result}")

    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
handle_multiple_exceptions()
