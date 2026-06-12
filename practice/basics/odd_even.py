# Problem Statement:
# Write a Python program to check whether a number is even or odd and separate even and odd numbers from a list.
#
# Intuition:
# A number is even when it is exactly divisible by 2.
#
# Input:
number = int(input("Enter a number: "))
numbers_input = input("Enter numbers separated by spaces: ")

# Logic:
# The modulo operator gives the remainder after division by 2.
if number % 2 == 0:
    result = "even"
else:
    result = "odd"

numbers = [int(value) for value in numbers_input.split()]
even_numbers = [value for value in numbers if value % 2 == 0]
odd_numbers = [value for value in numbers if value % 2 != 0]

# Output:
print(f"{number} is {result}.")
print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
