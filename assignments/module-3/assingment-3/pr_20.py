# 20) Write a Python program to show method overriding.


class Parent:
    def show_message(self):
        print("This message is from the Parent class.")

class Child(Parent):
    def show_message(self):
        print("This message is from the Child class.")

parent_obj = Parent()
parent_obj.show_message() 
child_obj = Child()
child_obj.show_message()   
