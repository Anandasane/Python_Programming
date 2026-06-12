# Problem Statement:
# Write a Python program to store and display variables of different data types.
#
# Intuition:
# Different values can be stored in variables, and the type() function shows each variable's data type.
#
# Input:
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

# Logic:
# Store the values in variables and check their data types.
person = {
    "name": name,
    "age": age,
    "height": height,
    "is_student": is_student,
}

# Output:
print("Person details:")
for key, value in person.items():
    print(f"{key}: {value} ({type(value).__name__})")
