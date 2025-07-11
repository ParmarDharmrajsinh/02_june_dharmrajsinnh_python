##Write a Python program to create a list with elements of multiple data types (integers, strings, floats, etc.). 




mixed_list = [42, "hello", 3.14, True, None, complex(2, 3)]
print("List with multiple data types:")
print(mixed_list)
print("\nElements and their data types:")
for element in mixed_list:
    print(f"{element} -> {type(element)}")
