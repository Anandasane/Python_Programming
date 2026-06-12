# Problem Statement:
# Write a Python program to check whether a year is a leap year.
#
# Intuition:
# A leap year is divisible by 4, except century years must be divisible by 400.
#
# Input:
year = int(input("Enter a year: "))

# Logic:
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    result = "leap year"
else:
    result = "not a leap year"

# Output:
print(f"{year} is a {result}.")
