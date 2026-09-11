from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height =height
    
    def area(self):
        print(f"the Area of the rectangle is {self.width * self.height}")
    
    def parameter(self):
        print(f"the parameter of the rectangle is {self.width*2+self.height*2}")

    
r=Rectangle(5,10)
r.area()
r.parameter()
