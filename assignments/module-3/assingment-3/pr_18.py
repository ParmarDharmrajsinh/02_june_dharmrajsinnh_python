#18) Write a Python program to demonstrate the use of super() in inheritance. 

class Parent:
    def __init__(self, name):
        self.name = name
        print(f"Parent constructor called. Name: {self.name}")

    def display(self):
        print(f"Hello, I am {self.name} from Parent class.")


class Child(Parent):
    def __init__(self, name, age):
        
        super().__init__(name)
        self.age = age
        print(f"Child constructor called. Age: {self.age}")

    def display(self):
        
        super().display()
        print(f"I am {self.age} years old, from Child class.")
child1 = Child("Dharmraj", 22)
child1.display()
