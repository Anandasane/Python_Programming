class Animal:
    def breathe(self): print("Breathing")

class Mammal(Animal):
    def feed_milk(self): print("Feeding milk")

class Bird(Animal):
    def fly(self): print("Flying")

class Dog(Mammal):
    def bark(self): print("Barking")

print(Dog.__mro__) 
