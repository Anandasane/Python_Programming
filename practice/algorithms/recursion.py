# Problem Statement:
# Write a Python program to calculate factorial, Fibonacci number, power, and list sum using recursion.
#
# Intuition:
# Recursion solves a problem by reducing it to a smaller version of the same problem.
#
# Input:
factorial_number = int(input("Enter number for factorial: "))
fibonacci_position = int(input("Enter Fibonacci position: "))
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
numbers_input = input("Enter numbers separated by spaces: ")

# Logic:
def factorial(value):
    if value in (0, 1):
        return 1
    return value * factorial(value - 1)


def fibonacci(position):
    if position <= 1:
        return position
    return fibonacci(position - 1) + fibonacci(position - 2)


def power(value_base, value_exponent):
    if value_exponent == 0:
        return 1
    return value_base * power(value_base, value_exponent - 1)


def recursive_sum(values):
    if not values:
        return 0
    return values[0] + recursive_sum(values[1:])


numbers = [int(value) for value in numbers_input.split()]
factorial_result = factorial(factorial_number)
fibonacci_result = fibonacci(fibonacci_position)
power_result = power(base, exponent)
sum_result = recursive_sum(numbers)

# Output:
print(f"Factorial of {factorial_number}: {factorial_result}")
print(f"Fibonacci number at position {fibonacci_position}: {fibonacci_result}")
print(f"{base} raised to {exponent}: {power_result}")
print(f"Recursive sum: {sum_result}")
