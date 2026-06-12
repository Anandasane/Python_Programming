# Problem Statement:
# Write a Python program to perform basic arithmetic operations.
#
# Intuition:
# Arithmetic operators such as +, -, *, /, and ** are used to calculate results from two numbers.
#
# Input:
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
base = float(input("Enter base for power: "))
exponent = int(input("Enter exponent for power: "))

# Logic:
addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number if second_number != 0 else "undefined"
power_result = base**exponent

# Output:
print(f"{first_number} + {second_number} = {addition}")
print(f"{first_number} - {second_number} = {subtraction}")
print(f"{first_number} * {second_number} = {multiplication}")
print(f"{first_number} / {second_number} = {division}")
print(f"{base} ** {exponent} = {power_result}")
