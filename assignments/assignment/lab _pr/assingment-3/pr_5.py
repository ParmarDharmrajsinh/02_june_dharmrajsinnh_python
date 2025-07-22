#5) Write a Python program to read a file and print the data on the console.

filename = "print_output.txt"

try:
    with open(filename, "r") as file:

        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print(f"File '{filename}' not found.")
