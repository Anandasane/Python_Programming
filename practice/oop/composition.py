# Problem Statement:
# Write a Python program to demonstrate composition using a car, engine, and wheels.
#
# Intuition:
# Composition builds complex objects by combining simpler objects.
#
# Input:
model = input("Enter car model: ")
horsepower = int(input("Enter engine horsepower: "))
wheel_size = int(input("Enter wheel size: "))

# Logic:
class Engine:
    def __init__(self, hp):
        self.horsepower = hp

    def start(self):
        return f"Engine with {self.horsepower} HP started"


class Wheel:
    def __init__(self, size):
        self.size = size

    def rotate(self):
        return f"{self.size}-inch wheel rotating"


class Car:
    def __init__(self, car_model, engine, wheels):
        self.model = car_model
        self.engine = engine
        self.wheels = wheels

    def drive(self):
        details = [self.engine.start()]
        details.extend(wheel.rotate() for wheel in self.wheels)
        details.append(f"{self.model} is driving")
        return details


engine = Engine(horsepower)
wheels = [Wheel(wheel_size) for _ in range(4)]
car = Car(model, engine, wheels)

# Output:
print("\n".join(car.drive()))
