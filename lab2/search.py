import re

mystr="this is python "

x=re.search("this", mystr)
print(x)  # This will print a match object if found, otherwise None

if x:
    print("Match found:", x.group())
else:
    print("No match found")