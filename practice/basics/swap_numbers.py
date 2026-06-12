# Problem Statement:
# Write a Python program to swap two numbers.
#
# Intuition:
# Python allows two variables to exchange values in a single assignment.
#
# Input:
first = input("Enter first value: ")
second = input("Enter second value: ")

# Logic:
# Swap the values using tuple unpacking.
first, second = second, first

# Output:
print(f"After swapping, first value: {first}")
print(f"After swapping, second value: {second}")
