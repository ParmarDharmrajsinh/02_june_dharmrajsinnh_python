#Write a Python program to write multiple strings into a file.

lines = [
    "Python is a powerful programming language.\n",
    "It is widely used in web development, data science, and more.\n",
    "File handling is an important part of Python programming.\n"
]

with open("multiple_lines.txt", "w") as file:

    file.writelines(lines)

print("Multiple lines written to 'multiple_lines.txt' successfully.")
