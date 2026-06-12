# Problem Statement:
# Write a Python program to demonstrate property decorators for controlled attribute access.
#
# Intuition:
# Property decorators allow validation while accessing or changing attribute values.
#
# Input:
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Logic:
class Temperature:
    def __init__(self, celsius_value):
        self._celsius = celsius_value

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("temperature below absolute zero is not possible")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9 / 5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5 / 9


temperature = Temperature(celsius)
temperature.fahrenheit = fahrenheit

# Output:
print(f"Celsius: {temperature.celsius:.2f}")
print(f"Fahrenheit: {temperature.fahrenheit:.2f}")
