#Write a Python program to apply the map() function to square a list of numbers. 

def square(Num):
    return Num*Num
numbers=[1,2,3,4,5]
squared_numbers=list(map(square,numbers))
print("original number:",numbers)
print("squared numbers:",squared_numbers)
