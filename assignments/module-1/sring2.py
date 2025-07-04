import math

while True:
    print("\n===== AREA CALCULATOR =====")
    print("1. Area of Square")
    print("2. Area of Circle")
    print("3. Area of Rectangle")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        side = float(input("Enter the side of the square: "))
        area = side * side
        print(f"Area of Square = {area:.2f}")

    elif choice == '2':
        radius = float(input("Enter the radius of the circle: "))
        area = math.pi * radius * radius
        print(f"Area of Circle = {area:.2f}")

    elif choice == '3':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        print(f"Area of Rectangle = {area:.2f}")

    elif choice == '4':
        print("Thank you! Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")