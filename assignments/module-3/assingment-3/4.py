#Write a Python program to read the contents of a file and print them on the console. 

with open("my_file.txt", "r") as file:
    content = file.read() 

print("File contents:\n")
print(content)
