# 3) Write a Python program to create a file and write a string into it

filename = "output.txt"

text_to_write = "Hello, this is a sample text written to a file."
with open(filename, "w") as file:
    file.write(text_to_write)

print(f"String has been written to '{filename}' successfully.")
