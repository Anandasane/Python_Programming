# Problem Statement:
# Write a Python program to check whether a number or string is a palindrome.
#
# Intuition:
# A palindrome reads the same forward and backward.
#
# Input:
value = input("Enter a number or text: ")

# Logic:
# Reverse the input string and compare it with the original string.
reversed_value = value[::-1]
is_palindrome = value == reversed_value

# Output:
print(f"Original value: {value}")
print(f"Reversed value: {reversed_value}")
print(f"Is palindrome? {is_palindrome}")
