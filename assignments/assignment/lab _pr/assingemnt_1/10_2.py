#Write a Python program that uses reduce() to find the product of a list of numbers. 

from functools import reduce

def multiple(x,y):
    return x*y

numbers=[1,2,3,4,5]

product=reduce(multiple,numbers)
print("list of numbers:",numbers)
print("product of all numbers:",product)
