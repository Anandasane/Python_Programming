# Problem Statement:
# Write a Python program to calculate area and perimeter of rectangle, circle, and triangle.
#
# Intuition:
# Use standard geometry formulas for each shape.
#
# Input:
length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))
radius = float(input("Enter circle radius: "))
base = float(input("Enter triangle base: "))
height = float(input("Enter triangle height: "))

# Logic:
rectangle_area = length * width
rectangle_perimeter = 2 * (length + width)
pi = 3.141592653589793
circle_area = pi * radius**2
circle_perimeter = 2 * pi * radius
triangle_area = 0.5 * base * height

# Output:
print(f"Rectangle area: {rectangle_area}")
print(f"Rectangle perimeter: {rectangle_perimeter}")
print(f"Circle area: {circle_area:.2f}")
print(f"Circle perimeter: {circle_perimeter:.2f}")
print(f"Triangle area: {triangle_area}")
