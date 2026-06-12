# Problem Statement:
# Write a Python program to demonstrate operator overloading using a vector class.
#
# Intuition:
# Special methods such as __add__, __sub__, and __mul__ define how operators work for custom objects.
#
# Input:
first_x = int(input("Enter first vector x: "))
first_y = int(input("Enter first vector y: "))
second_x = int(input("Enter second vector x: "))
second_y = int(input("Enter second vector y: "))
scalar = int(input("Enter scalar value: "))

# Logic:
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, value):
        return Vector(self.x * value, self.y * value)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


first = Vector(first_x, first_y)
second = Vector(second_x, second_y)
addition = first + second
subtraction = first - second
multiplication = first * scalar

# Output:
print(f"first + second = {addition}")
print(f"first - second = {subtraction}")
print(f"first * scalar = {multiplication}")
