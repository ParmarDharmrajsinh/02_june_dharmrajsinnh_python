# 16) Write a Python program to show hierarchical inheritance
class Animal:
    def sound(self):
        print("Animals make different sounds.")
class Dog(Animal):
    def bark(self):
        print("Dog barks.")
class Cat(Animal):
    def meow(self):
        print("Cat meows.")
dog1 = Dog()
cat1 = Cat()

print("Dog Object:")
dog1.sound()   
dog1.bark()   

print("\nCat Object:")
cat1.sound()   
cat1.meow()    
