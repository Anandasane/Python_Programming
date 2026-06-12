# Problem Statement:
# Write a Python program to perform addition, multiplication, and factorial using functions.
#
# Intuition:
# Functions make reusable blocks of code for repeated calculations.
#
# Input:
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
factorial_number = int(input("Enter number for factorial: "))

# Logic:
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def factorial(number):
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


sum_result = add(first_number, second_number)
product_result = multiply(first_number, second_number)
factorial_result = factorial(factorial_number)

# Output:
print(f"{first_number} + {second_number} = {sum_result}")
print(f"{first_number} * {second_number} = {product_result}")
print(f"Factorial of {factorial_number} = {factorial_result}")
