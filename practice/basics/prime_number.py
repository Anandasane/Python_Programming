# Problem Statement:
# Write a Python program to check whether a number is prime and print all prime numbers up to a limit.
#
# Intuition:
# A prime number has exactly two factors: 1 and itself.
#
# Input:
number = int(input("Enter a number: "))
limit = int(input("Enter limit to print primes: "))

# Logic:
def is_prime(value):
    if value < 2:
        return False
    for divisor in range(2, int(value**0.5) + 1):
        if value % divisor == 0:
            return False
    return True


prime_check = is_prime(number)
prime_numbers = [value for value in range(2, limit + 1) if is_prime(value)]

# Output:
print(f"Is {number} prime? {prime_check}")
print(f"Prime numbers up to {limit}: {prime_numbers}")
