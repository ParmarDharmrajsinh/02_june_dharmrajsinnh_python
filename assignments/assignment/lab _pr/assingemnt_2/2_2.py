## Write a Python program to remove elements from a list using pop() and remove(). 

# Python program to remove elements from a list using pop() and remove()

# Initial list of fruits
fruits = ['apple', 'banana', 'cherry', 'date', 'fig']

print("Original list:")
print(fruits)

# Using pop() to remove elements by index
popped_item = fruits.pop(2)  # Removes 'cherry' at index 2
print("\nAfter pop(2):")
print(fruits)
print("Popped item:", popped_item)

# Using remove() to remove elements by value
fruits.remove('banana')  # Removes 'banana' from the list
print("\nAfter remove('banana'):")
print(fruits)

# Attempting to remove an item that does not exist