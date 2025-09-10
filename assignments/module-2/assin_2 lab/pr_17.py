#16) Write a Python program to separate keys and values from a dictionary using keys() and values() methods.

student = {
    "name": "Dharmraj",
    "age": 21,
    "course": "Computer Science",
    "grade": "A"
}
keys = student.keys()
values = student.values()
print("Dictionary:", student)
print("\nKeys:", keys)
print("Values:", values)
keys_list = list(keys)
values_list = list(values)
print("\nKeys as List:", keys_list)
print("Values as List:", values_list)
