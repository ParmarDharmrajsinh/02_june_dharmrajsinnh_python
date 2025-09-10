# 15) Write a Python program to show multiple inheritance.

class Father:
    def skills(self):
        print("Father's skills: Gardening, Carpentry")
class Mother:
    def skills(self):
        print("Mother's skills: Cooking, Painting")
class Child(Father, Mother):
    def skills(self):
        print("Child's skills: Singing, Dancing")
        Father.skills(self)
        Mother.skills(self)
child1 = Child()
child1.skills()
