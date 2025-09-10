#13) Write a Python program to create a dictionary of 6 key-value pairs.
mydict={"name":"niitn",
        "age":21,
        "city":"rajkot"}

print(mydict)

for key,value in mydict.items():
    print(f"key: {key},value: {value}")
