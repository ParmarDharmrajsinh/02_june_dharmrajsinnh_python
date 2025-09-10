#Write a Python program that filters out even numbers using the filter() function.

from functools import reduce

def multiply(x,y):
    return x*y

numbers=[1,2,3,4,5]

product=reduce(multiply,numbers)
print("product of all numbers:",product)