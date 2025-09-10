#Write a Python program to demonstrate string slicing. 

text="python programing"

print("original string:",text)
print("slice from index 0 to 5:",text[0:6])
print("slice from index 6 to end1:",text[6:])
print("slice from start to index 5:",text[6:])
print("last 3 characters:",text[-3:])
print("full string reversed:",text[::-1])
print("every second charcter:",text[::2])
print("characters from index 2 to 10 with step:",text[2:11:2])