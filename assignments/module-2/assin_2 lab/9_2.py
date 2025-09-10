#Write a Python program to generate random numbers using the random module.
import random 
random_int = random.randint(1, 100)
print("Random Integer (1 to 100):", random_int)
random_float = random.random()
print("Random Float (0 to 1):", random_float)
random_uniform = random.uniform(10.5, 50.5)
print("Random Float (10.5 to 50.5):", random_uniform)
