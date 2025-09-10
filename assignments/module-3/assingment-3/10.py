#Write a Python program to search for a word in a string using re.search(). 


import re
text = "Python is a powerful programming language."
word = input("Enter the word to search: ")
if re.search(rf'\b{re.escape(word)}\b', text):
    print(f"✅ The word '{word}' was found in the string.")
else:
    print(f"❌ The word '{word}' was NOT found in the string.")
