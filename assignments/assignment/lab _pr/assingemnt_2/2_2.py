## Write a Python program to remove elements from a list using pop() and remove(). 


fruits = ['apple', 'banana', 'cherry', 'date', 'fig']
print("Original list:")
print(fruits)
popped_item = fruits.pop(2)  
print("\nAfter pop(2):")
print(fruits)
print("Popped item:", popped_item)
fruits.remove('banana') 
print("\nAfter remove('banana'):")
print(fruits)

