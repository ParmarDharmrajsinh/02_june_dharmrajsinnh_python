#Write a Python program that demonstrates the correct use of indentation, comments, and variables following PEP 8 guidelines




FAHRENHEIT_MULTIPLIER = 9 / 5
FAHRENHEIT_OFFSET = 32


celsius_temperature = float(input("Enter temperature in Celsius: "))


fahrenheit_temperature = (celsius_temperature * FAHRENHEIT_MULTIPLIER) + FAHRENHEIT_OFFSET


print(f"{celsius_temperature}°C is equal to {fahrenheit_temperature}°F")
