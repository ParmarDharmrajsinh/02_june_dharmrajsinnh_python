##Write a Python program to create a tuple with multiple data types. 

mixed_tuple = (25, "Python", 3.14, True, None, complex(2, -3))
print("Tuple with multiple data types:")
print(mixed_tuple)
print("\nElements and their data types:")
for element in mixed_tuple:
    print(f"{element} -> {type(element)}")
