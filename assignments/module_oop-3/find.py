import re

mystr="this is python "

x=re.findall("is", mystr)
print(x)  # This will print a match object if found, otherwise None

if x:
    print("Match found:")
else:
    print("No match found")