# Problem Statement:
# Write a Python program to convert between binary, decimal, octal, and hexadecimal number systems.
#
# Intuition:
# Python has built-in conversion functions and int() can parse a string in a given base.
#
# Input:
binary_value = input("Enter a binary number: ")
decimal_value = int(input("Enter a decimal number: "))

# Logic:
decimal_from_binary = int(binary_value, 2)
binary_from_decimal = bin(decimal_value)[2:]
octal_from_decimal = oct(decimal_value)[2:]
hexadecimal_from_decimal = hex(decimal_value)[2:].upper()

# Output:
print(f"Binary {binary_value} to decimal: {decimal_from_binary}")
print(f"Decimal {decimal_value} to binary: {binary_from_decimal}")
print(f"Decimal {decimal_value} to octal: {octal_from_decimal}")
print(f"Decimal {decimal_value} to hexadecimal: {hexadecimal_from_decimal}")
