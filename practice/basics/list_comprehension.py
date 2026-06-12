# Problem Statement:
# Write a Python program to create lists using list comprehension.
#
# Intuition:
# List comprehension creates a new list in a short and readable way.
#
# Input:
limit = int(input("Enter limit: "))

# Logic:
squares = [number**2 for number in range(1, limit + 1)]
even_squares = [number**2 for number in range(1, limit + 1) if number % 2 == 0]
pairs = [(first, second) for first in range(1, 4) for second in range(1, 4)]

# Output:
print(f"Squares up to {limit}: {squares}")
print(f"Even squares up to {limit}: {even_squares}")
print(f"Pairs from 1 to 3: {pairs}")
