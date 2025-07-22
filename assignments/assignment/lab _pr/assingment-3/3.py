# Write a Python program to open a file in write mode, write some text, and then close it.

with open("my_file.txt", "w") as file:
    file.write("Hello, this is a sample text file.\n")
    file.write("Writing to a file in Python is easy!\n")

print("Text written to 'my_file.txt' successfully.")
