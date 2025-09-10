#11) Write a Python program to create a class and access the properties of the class using an object. 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
person1 = Person("Alice", 25)
print("Accessing properties using the object:")
print("Name:", person1.name)
print("Age:", person1.age)
print("\nUsing class method to display info:")
person1.display_info()
