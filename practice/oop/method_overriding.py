# Problem Statement:
# Write a Python program to demonstrate method overriding.
#
# Intuition:
# A child class can provide its own version of a method already defined in the parent class.
#
# Input:
vehicle_type = input("Enter vehicle type (vehicle/car/bicycle): ")

# Logic:
class Vehicle:
    def start(self):
        return "Vehicle started"

    def stop(self):
        return "Vehicle stopped"


class Car(Vehicle):
    def start(self):
        return "Car engine started with key"

    def play_music(self):
        return "Music playing"


class Bicycle(Vehicle):
    def start(self):
        return "Bicycle started by pedaling"


if vehicle_type == "car":
    vehicle = Car()
elif vehicle_type == "bicycle":
    vehicle = Bicycle()
else:
    vehicle = Vehicle()

# Output:
print(vehicle.start())
print(vehicle.stop())
if isinstance(vehicle, Car):
    print(vehicle.play_music())
