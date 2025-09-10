# 15) Write a Python program to update a value at a particular key in a dictionary. 
student = {
    "name": "Dharmraj",
    "age": 21,
    "course": "Computer Science",
    "grade": "A"
}
print("Original Dictionary:")
print(student)
student["age"] = 22  
student["grade"] = "A+"  
print("\nUpdated Dictionary:")
print(student)
student.update({"course": "Data Science"})
print("\nAfter update() method:")
print(student)



