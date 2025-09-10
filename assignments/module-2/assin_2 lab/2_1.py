##Write a Python program to add elements to a list using insert() and append(). 

fruits = []
fruits.append("apple")
fruits.append("banana")
fruits.append("cherry")
print("List after using append():")
print(fruits)
fruits.insert(0, "mango")     
fruits.insert(2, "orange")
print("\nList after using insert():")
print(fruits)
