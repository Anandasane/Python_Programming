# Problem Statement:
# Write a Python program to check whether a number is a perfect number and print perfect numbers up to a limit.
#
# Intuition:
# A perfect number equals the sum of its proper divisors.
#
# Input:
number = int(input("Enter a number: "))
limit = int(input("Enter limit: "))

# Logic:
def is_perfect(value):
    if value < 2:
        return False
    divisor_sum = sum(divisor for divisor in range(1, value) if value % divisor == 0)
    return divisor_sum == value


perfect_check = is_perfect(number)
perfect_numbers = [value for value in range(2, limit + 1) if is_perfect(value)]

# Output:
print(f"Is {number} a perfect number? {perfect_check}")
print(f"Perfect numbers up to {limit}: {perfect_numbers}")
