# Problem Statement:
# Write a Python program to convert temperatures between Celsius, Fahrenheit, and Kelvin.
#
# Intuition:
# Use standard temperature conversion formulas.
#
# Input:
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
kelvin = float(input("Enter temperature in Kelvin: "))

# Logic:
celsius_to_fahrenheit = (celsius * 9 / 5) + 32
fahrenheit_to_celsius = (fahrenheit - 32) * 5 / 9
celsius_to_kelvin = celsius + 273.15
kelvin_to_celsius = kelvin - 273.15

# Output:
print(f"{celsius} C = {celsius_to_fahrenheit:.2f} F")
print(f"{fahrenheit} F = {fahrenheit_to_celsius:.2f} C")
print(f"{celsius} C = {celsius_to_kelvin:.2f} K")
print(f"{kelvin} K = {kelvin_to_celsius:.2f} C")
