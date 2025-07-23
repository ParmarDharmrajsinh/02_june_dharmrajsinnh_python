#14) Write a Python program to show multilevel inheritance.

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")
class Puppy(Dog):
    def weep(self):
        print(f"{self.name} is weeping.")
puppy1 = Puppy("Tommy")
puppy1.eat()   
puppy1.bark()  
puppy1.weep()  
