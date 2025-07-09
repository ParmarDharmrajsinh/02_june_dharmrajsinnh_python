##Write a Python program to add elements to a list using insert() and append(). 

# Python program to add elements to a list using insert() and append()

# Creating an empty list
fruits = []

# Using append() to add elements at the end of the list
fruits.append("apple")
fruits.append("banana")
fruits.append("cherry")

print("List after using append():")
print(fruits)

# Using insert() to add elements at specific positions
fruits.insert(0, "mango")     # Insert at the beginning
fruits.insert(2, "orange")    # Insert at index 2

print("\nList after using insert():")
print(fruits)
