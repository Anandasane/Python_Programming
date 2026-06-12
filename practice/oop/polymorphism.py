# Problem Statement:
# Write a Python program to demonstrate polymorphism using different shapes.
#
# Intuition:
# Different classes can implement the same method name in their own way.
#
# Input:
shape_type = input("Enter shape type (rectangle/circle): ")

# Logic:
class Shape:
    def area(self):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.141592653589793 * self.radius**2


if shape_type == "rectangle":
    length = float(input("Enter rectangle length: "))
    width = float(input("Enter rectangle width: "))
    shape = Rectangle(length, width)
else:
    radius = float(input("Enter circle radius: "))
    shape = Circle(radius)

# Output:
print(f"Selected shape: {shape_type}")
print(f"Area: {shape.area():.2f}")
