# 18) Write a Python program to count how many times each character appears in a string. 


text = "programming in python"

char_count = {}

for char in text:
    if char != " ":  
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

print("Character frequency in the string:")
for key, value in char_count.items():
    print(f"{key} : {value}")
