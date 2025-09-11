# 17) Write a Python program to show hybrid inheritance. 

class Person:
    def display_person(self):
        print("I am a Person.")


class Student(Person):
    def display_student(self):
        print("I am a Student.")

class Artist:
    def display_artist(self):
        print("I am an Artist.")

class MultiTalentedStudent(Student, Artist):
    def display_multitalented(self):
        print("I am a Multi-Talented Student.")


mts = MultiTalentedStudent()


mts.display_person()          
mts.display_student()          
mts.display_artist()           
mts.display_multitalented()    