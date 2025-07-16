import re

mystr="This Is python "

x=re.findall("[A-Z]",mystr)
#[a-za-z] for lowercase letters
#[a-za-z0-9] for alphanumeric characters
print(x)