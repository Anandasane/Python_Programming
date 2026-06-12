# Problem Statement:
# Write a Python program to calculate percentage and grade from marks.
#
# Intuition:
# Percentage is obtained by dividing obtained marks by total marks and multiplying by 100.
#
# Input:
marks_input = input("Enter marks separated by spaces: ")
total_marks = float(input("Enter total marks: "))

# Logic:
marks = [float(value) for value in marks_input.split()]
percentage = (sum(marks) / total_marks) * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Output:
print(f"Marks: {marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
