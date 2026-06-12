# Problem Statement:
# Write a Python program to store values in a tuple, access tuple elements, and unpack a tuple.
#
# Intuition:
# Tuples are ordered and immutable, so they are useful for fixed collections of values.
#
# Input:
number = int(input("Enter a number: "))
text = input("Enter text: ")
decimal = float(input("Enter a decimal value: "))
boolean_text = input("Enter True or False: ").lower() == "true"

# Logic:
values = (number, text, decimal, boolean_text)
unpacked_number, unpacked_text, unpacked_decimal, unpacked_boolean = values

# Output:
print(f"Tuple: {values}")
print(f"First value: {unpacked_number}")
print(f"Last value: {unpacked_boolean}")
print(f"Unpacked values: {unpacked_number}, {unpacked_text}, {unpacked_decimal}, {unpacked_boolean}")
