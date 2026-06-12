# Problem Statement:
# Write a Python program to perform basic calculator operations.
#
# Intuition:
# Choose the operation based on the operator entered by the user.
#
# Input:
first_number = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
second_number = float(input("Enter second number: "))

# Logic:
if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    if second_number == 0:
        result = "Division by zero is not allowed."
    else:
        result = first_number / second_number
else:
    result = "Invalid operator."

# Output:
print(f"Result: {result}")
