#Write a Python program to import the math module and use functions like sqrt(), ceil(), floor(). 


import math
num = float(input("Enter a number: "))
square_root = math.sqrt(num)
ceil_value = math.ceil(num)
floor_value = math.floor(num)
print(f"\nSquare root of {num} is: {square_root}")
print(f"Ceiling of {num} is: {ceil_value}")
print(f"Floor of {num} is: {floor_value}")
