# Problem Statement:
# Write a Python program to check a grade based on marks and classify a number as positive, negative, or zero.
#
# Intuition:
# Use if-elif-else conditions to choose the correct output based on the input value.
#
# Input:
score = int(input("Enter score: "))
number = int(input("Enter a number: "))

# Logic:
# Grade is decided by score ranges.
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# A number greater than 0 is positive, less than 0 is negative, otherwise it is zero.
if number > 0:
    number_type = "positive"
elif number < 0:
    number_type = "negative"
else:
    number_type = "zero"

# Output:
print(f"Grade for score {score}: {grade}")
print(f"{number} is {number_type}.")
