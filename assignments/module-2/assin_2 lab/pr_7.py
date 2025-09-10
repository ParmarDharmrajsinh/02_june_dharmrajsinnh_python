#  6) Write a Python program to insert elements into an empty list using a for loop and append(). 
list=[]

n=int(input("how many elements u want to insrt:"))

for i in range(n):
    i=input("enter value of your element:")
    list.append(i)
print(list)

