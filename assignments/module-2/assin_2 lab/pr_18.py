# Program to convert two lists into a dictionary using a for loop


keys = ["name", "age", "course", "grade"]
values = ["Dharmraj", 21, "Computer Science", "A"]

student = {}

for i in range(len(keys)):
    student[keys[i]] = values[i]

print("Dictionary created from two lists:")
print(student)
