# Problem Statement:
# Write a Python program to print the multiplication table of a number.
#
# Intuition:
# Multiply the given number by values from 1 to the table limit.
#
# Input:
number = int(input("Enter a number: "))
limit = int(input("Enter table limit: "))

# Logic:
table = [number * multiplier for multiplier in range(1, limit + 1)]

# Output:
print(f"Multiplication table of {number} up to {limit}: {table}")
