# 24) Write a Python program to generate random numbers between 1 and 100 using the random module. 


import random

num = random.randint(1, 100)
print("Random number (1 to 100):", num)

print("\nFive random numbers between 1 and 100:")
for i in range(5):
    print(random.randint(1, 100))
