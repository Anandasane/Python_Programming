# Problem Statement:
# Write a Python program to calculate sum, factorial, and power using recursion.
#
# Intuition:
# Recursion solves a problem by calling the same function on a smaller version of the problem.
#
# Input:
number = int(input("Enter a positive number: "))
factorial_number = int(input("Enter number for factorial: "))
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

# Logic:
def recursive_sum(value):
    if value <= 1:
        return value
    return value + recursive_sum(value - 1)


def recursive_factorial(value):
    if value in (0, 1):
        return 1
    return value * recursive_factorial(value - 1)


def recursive_power(value_base, value_exponent):
    if value_exponent == 0:
        return 1
    return value_base * recursive_power(value_base, value_exponent - 1)


sum_result = recursive_sum(number)
factorial_result = recursive_factorial(factorial_number)
power_result = recursive_power(base, exponent)

# Output:
print(f"Recursive sum up to {number}: {sum_result}")
print(f"Recursive factorial of {factorial_number}: {factorial_result}")
print(f"{base} raised to {exponent}: {power_result}")
