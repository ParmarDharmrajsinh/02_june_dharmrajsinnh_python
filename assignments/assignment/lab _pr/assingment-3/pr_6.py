#6) Write a Python program to check the current position of the file cursor using tell()

filename = "cursor_example.txt"

with open(filename, "w") as file:
    file.write("Hello, World!")
with open(filename, "r") as file:
    position = file.tell()
    print(f"Initial cursor position: {position}")
    file.read(5)
    position = file.tell()
    print(f"Cursor position after reading 5 characters: {position}")
