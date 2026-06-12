# Problem Statement:
# Write a Python program to demonstrate constructors by calculating rectangle and circle measurements.
#
# Intuition:
# A constructor initializes object data when an object is created.
#
# Input:
rectangle_length = float(input("Enter rectangle length: "))
rectangle_width = float(input("Enter rectangle width: "))
circle_radius = float(input("Enter circle radius: "))

# Logic:
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.141592653589793 * self.radius**2

    def perimeter(self):
        return 2 * 3.141592653589793 * self.radius


rectangle = Rectangle(rectangle_length, rectangle_width)
circle = Circle(circle_radius)

# Output:
print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")
print(f"Circle area: {circle.area():.2f}")
print(f"Circle perimeter: {circle.perimeter():.2f}")
