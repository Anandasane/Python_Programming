print('============================================Abstraction======================================================')

'''Abstraction is one of the core concepts of Object-Oriented Programming (OOP). It 
means hiding complex implementation details and showing only the essential features 
to the user.'''

from abc import ABC, abstractmethd

class Shape(ABC):
    @abstractmethd
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        