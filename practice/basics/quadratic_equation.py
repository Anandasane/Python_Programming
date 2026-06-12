# Problem Statement:
# Write a Python program to find the roots of a quadratic equation.
#
# Intuition:
# The quadratic formula finds roots using the discriminant b² - 4ac.
#
# Input:
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Logic:
import cmath

discriminant = b**2 - 4 * a * c
root_value = cmath.sqrt(discriminant)
root1 = (-b + root_value) / (2 * a)
root2 = (-b - root_value) / (2 * a)

# Output:
print(f"Equation: {a}x² + {b}x + {c} = 0")
print(f"Root 1: {root1}")
print(f"Root 2: {root2}")
