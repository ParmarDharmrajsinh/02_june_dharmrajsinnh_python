# Write Python programs to demonstrate method overloading and method overriding.

class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c
calc = Calculator()

print("add(2, 3):", calc.add(2, 3))
print("add(1, 4, 5):", calc.add(1, 4, 5))
print("add():", calc.add())
