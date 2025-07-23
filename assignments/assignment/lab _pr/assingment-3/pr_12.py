#12) Write a Python program to demonstrate the use of local and global variables in a class. 

school_name = "Green Valley School"

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show_details(self):
        section = "A"
        print(f"Student Name: {self.name}")
        print(f"Grade: {self.grade}")
        print(f"Section (local variable): {section}")
        print(f"School (global variable): {school_name}")
student1 = Student("John", "7th")
student1.show_details()
print("\nAccessing global variable outside the class:")
print("School Name:", school_name)
