# 4) Write a Python program to create a file and print the string into the file.

filename = "print_output.txt"
with open(filename, "w") as file:

    print("This string is printed into the file using the print() function.", file=file)

print(f"String has been printed to '{filename}' successfully.")
