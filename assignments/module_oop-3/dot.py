import re

mystr="This Is python "

#x=re.findall("py..on",mystr)
x=re.findall("This|that",mystr)
print(x)