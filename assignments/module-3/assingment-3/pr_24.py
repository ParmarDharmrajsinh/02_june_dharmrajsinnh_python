# 24) Write a Python program to match a word in a string using re.match().

import re

text = "Python is a powerful programming language."
word_to_match = "Python"

match = re.match(word_to_match, text)

if match:
    print(f"'{word_to_match}' matches at the beginning of the string.")
else:
    print(f"'{word_to_match}' does NOT match at the beginning of the string.")
