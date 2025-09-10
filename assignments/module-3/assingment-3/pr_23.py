#23) Write a Python program to search for a word in a string using re.search().
import re

text = "Hello, my name is Dharmraj Parmar and I love Python programming."

word_to_search = "Python"

match = re.search(word_to_search, text)

if match:
    print(f"'{word_to_search}' found in the string at position {match.start()} to {match.end()}")
else:
    print(f"'{word_to_search}' not found in the string.")
