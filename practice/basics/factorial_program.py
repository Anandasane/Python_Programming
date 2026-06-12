# Problem Statement:
# Write a Python program to find the factorial of a number.
#
# Intuition:
# Factorial of n is the product of all positive integers from 1 to n.
#
# Input:
number = int(input("Enter a number: "))

# Logic:
# Start with 1 and multiply it by every number from 2 to the entered number.
if number < 0:
    result = "Factorial is not defined for negative numbers."
else:
    factorial_value = 1
    for value in range(2, number + 1):
        factorial_value *= value
    result = factorial_value

# Output:
print(result if isinstance(result, str) else f"Factorial of {number} = {result}")
