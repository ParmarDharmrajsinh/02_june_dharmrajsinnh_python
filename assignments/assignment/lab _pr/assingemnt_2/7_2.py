##Write a Python program to merge two lists into one dictionary using a loop. 
keys = ['name', 'age', 'course', 'grade']
values = ['Alice', 22, 'Mathematics', 'A']
merged_dict = {}
for i in range(len(keys)):
    merged_dict[keys[i]] = values[i]
print("Merged Dictionary:")
print(merged_dict)
