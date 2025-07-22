#Write a Python program to create a class and access its properties using an object. 

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student1 = Student("Dharmrajsinh", 22, "Python Programming")
print("Student Details:")
print(f"Name   : {student1.name}")
print(f"Age    : {student1.age}")
print(f"Course : {student1.course}")
