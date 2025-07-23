# Write a Python program to handle file exceptions and use the finally block for closing the file. 

try:
    file_name = input("Enter the file name to read: ")
    file = open(file_name, 'r')  
    content = file.read()
    print("\n--- File Content ---")
    print(content)

except FileNotFoundError:
    print(f"\nError: The file '{file_name}' was not found.")

except IOError:
    print("\nError: An I/O error occurred while reading the file.")

finally:
    try:
        file.close()
        print("\nFile closed successfully.")
    except NameError:
        print("\nFile was never opened, so no need to close.")
