# Problem Statement:
# Write a Python program to check whether a number is an Armstrong number and print Armstrong numbers up to a limit.
#
# Intuition:
# An Armstrong number equals the sum of its digits raised to the power of the number of digits.
#
# Input:
number = int(input("Enter a number: "))
limit = int(input("Enter limit: "))

# Logic:
def is_armstrong(value):
    digits = str(value)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == value


armstrong_check = is_armstrong(number)
armstrong_numbers = [value for value in range(limit + 1) if is_armstrong(value)]

# Output:
print(f"Is {number} an Armstrong number? {armstrong_check}")
print(f"Armstrong numbers up to {limit}: {armstrong_numbers}")
