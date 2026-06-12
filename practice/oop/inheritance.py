# Problem Statement:
# Write a Python program to demonstrate inheritance using animals.
#
# Intuition:
# A child class can reuse and modify behavior from a parent class.
#
# Input:
dog_name = input("Enter dog name: ")
cat_name = input("Enter cat name: ")

# Logic:
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"


animals = [Dog(dog_name), Cat(cat_name)]
sounds = [animal.speak() for animal in animals]

# Output:
print("\n".join(sounds))
