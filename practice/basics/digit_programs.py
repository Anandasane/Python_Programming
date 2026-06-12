# Problem Statement:
# Write a Python program to find the sum of digits, count digits, and reverse a number.
#
# Intuition:
# Converting the number to a string makes each digit easy to access.
#
# Input:
number = int(input("Enter a number: "))

# Logic:
absolute_number = abs(number)
digits = str(absolute_number)
sum_of_digits = sum(int(digit) for digit in digits)
digit_count = len(digits)
sign = -1 if number < 0 else 1
reversed_number = sign * int(digits[::-1])

# Output:
print(f"Number: {number}")
print(f"Sum of digits: {sum_of_digits}")
print(f"Count of digits: {digit_count}")
print(f"Reversed number: {reversed_number}")
