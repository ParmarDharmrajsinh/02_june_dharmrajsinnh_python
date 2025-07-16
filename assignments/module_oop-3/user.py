import re 
username="parmar@gmail.com"

username_pattern="[a-z0-9]+@+gmail|yahoo + .com|.in"

x=re.findall(username_pattern, username)

if x:
    print("Valid username:", x)
else:
    print("Invalid username")