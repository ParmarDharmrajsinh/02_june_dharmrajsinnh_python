#Write a Python program to match a word in a string using re.match().

import re
text = "Python is a powerful programming language."
word = input("Enter the word to match: ")
if re.match(rf'\b{re.escape(word)}\b', text):
    print(f"✅ The string starts with the word '{word}'.")
else:
    print(f"❌ The string does NOT start with the word '{word}'.")
