def handle_multiple_exceptions():
    try:
        
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        
        result = num1 / num2
        print(f"Result of division: {result}")

        
        sample_list = [10, 20, 30]
        index = int(input("Enter index to access (0-2): "))
        print(f"Element at index {index}: {sample_list[index]}")

    except ValueError:
        print("❌ Invalid input! Please enter integers only.")
    except ZeroDivisionError:
        print("❌ Cannot divide by zero.")
    except IndexError:
        print("❌ Index out of range! Please enter 0, 1, or 2.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
handle_multiple_exceptions()
