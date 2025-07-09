#Write a Python program to sort a list using both sort() and sorted(). 

# Python program to sort a list using sort() and sorted()

# Original list of numbers
numbers = [42, 17, 8, 99, 23, 4]

print("Original list:")
print(numbers)

# Using sort() - modifies the original list
numbers.sort()
print("\nList after sort():")
print(numbers)

# Re-creating the original list
numbers = [42, 17, 8, 99, 23, 4]

# Using sorted() - returns a new sorted list, does not change original
sorted_list = sorted(numbers)
print("\nList after sorted():")
print("Original list remains unchanged:", numbers)
print("New sorted list:", sorted_list)
