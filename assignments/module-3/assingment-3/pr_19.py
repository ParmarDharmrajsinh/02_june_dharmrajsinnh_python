# 19) Write a Python program to show method overloading. 


class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print("Sum of 2 numbers:", calc.add(5, 10))
print("Sum of 3 numbers:", calc.add(5, 10, 15))
