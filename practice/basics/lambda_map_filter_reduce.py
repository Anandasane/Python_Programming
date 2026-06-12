# Problem Statement:
# Write a Python program to use map, filter, lambda, and reduce.
#
# Intuition:
# map transforms each item, filter keeps selected items, lambda creates small functions, and reduce combines values.
#
# Input:
numbers_input = input("Enter numbers separated by spaces: ")

# Logic:
from functools import reduce

numbers = [int(value) for value in numbers_input.split()]
squared = list(map(lambda value: value**2, numbers))
doubled = list(map(lambda value: value * 2, numbers))
even_numbers = list(filter(lambda value: value % 2 == 0, numbers))
product = reduce(lambda total, value: total * value, numbers)

# Output:
print(f"Numbers: {numbers}")
print(f"Squared numbers: {squared}")
print(f"Doubled numbers: {doubled}")
print(f"Even numbers: {even_numbers}")
print(f"Product: {product}")
