# Problem Statement:
# Write a Python program to demonstrate method overloading behavior in Python.
#
# Intuition:
# Python supports flexible argument handling using *args, allowing one method to accept different numbers of values.
#
# Input:
numbers_input = input("Enter numbers separated by spaces: ")

# Logic:
class Calculator:
    def add(self, *values):
        total = 0
        for value in values:
            total += value
        return total

    def multiply(self, *values):
        total = 1
        for value in values:
            total *= value
        return total


calculator = Calculator()
numbers = [float(value) for value in numbers_input.split()]
add_result = calculator.add(*numbers)
multiply_result = calculator.multiply(*numbers)

# Output:
print(f"Sum: {add_result}")
print(f"Product: {multiply_result}")
