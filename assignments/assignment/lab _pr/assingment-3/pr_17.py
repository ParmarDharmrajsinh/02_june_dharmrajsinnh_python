# 17) Write a Python program to show hybrid inheritance. 




# Base class
class Person:
    def display_person(self):
        print("I am a Person.")

# First child class (Single Inheritance from Person)
class Student(Person):
    def display_student(self):
        print("I am a Student.")

# Another independent base class
class Artist:
    def display_artist(self):
        print("I am an Artist.")

# Hybrid: Inherits from both Student (which inherits Person) and Artist
class MultiTalentedStudent(Student, Artist):
    def display_multitalented(self):
        print("I am a Multi-Talented Student.")

# Create an object of MultiTalentedStudent
mts = MultiTalentedStudent()

# Call methods from all classes
mts.display_person()           # From Person (via Student)
mts.display_student()          # From Student
mts.display_artist()           # From Artist
mts.display_multitalented()    # From MultiTalentedStudent
