#Write a Python program to sort a list using both sort() and sorted(). 

numbers = [42, 17, 8, 99, 23, 4]
print("Original list:")
print(numbers)
numbers.sort()
print("\nList after sort():")
print(numbers)
numbers = [42, 17, 8, 99, 23, 4]
sorted_list = sorted(numbers)
print("\nList after sorted():")
print("Original list remains unchanged:", numbers)
print("New sorted list:", sorted_list)
