#23) Write a Python program to demonstrate the use of functions from the math module. 


import math

num = 25
angle = 30 
print("Square root of", num, "is:", math.sqrt(num))
print("Factorial of 5 is:", math.factorial(5))
print("2 raised to power 3 is:", math.pow(2, 3))
print("Value of pi:", math.pi)
print("Value of e:", math.e)

radian = math.radians(angle)
print("\n30 degrees in radians is:", radian)


print("sin(30°) =", math.sin(radian))
print("cos(30°) =", math.cos(radian))
print("tan(30°) =", math.tan(radian))

print("\nCeiling of 4.3 is:", math.ceil(4.3))
print("Floor of 4.7 is:", math.floor(4.7))
print("Absolute value of -10 is:", math.fabs(-10))
