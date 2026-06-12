# Problem Statement:
# Write a Python program to handle division errors and invalid integer input safely.
#
# Intuition:
# Try-except blocks catch runtime errors and prevent the program from crashing.
#
# Input:
numerator = float(input("Enter numerator: "))
denominator = float(input("Enter denominator: "))
integer_text = input("Enter an integer as text: ")

# Logic:
try:
    division_result = numerator / denominator
except ZeroDivisionError:
    division_result = None

try:
    parsed_integer = int(integer_text)
except ValueError:
    parsed_integer = None

# Output:
print(f"Division result: {division_result}")
print(f"Parsed integer: {parsed_integer}")
