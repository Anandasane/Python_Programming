print('===========================================polymorphism=====================================================')
print('===========================================overloading======================================================')

class Function:

    def add(self,a=0,b=0,c=0):
        print(a+b+c)
        print(2)

f=Function()
f.add(13,21)


print('===========================================overriding======================================================')
class A:
    def show(self):
        print("In A")

class B(A):
    def show(self):
        print("In B")


b=B()
b.show()

a=A()
a.show()

print('============================================operator overloading======================================================')

class Student:
    def __init__(self, marks):
        self.marks=marks

    def __add__(self, other):
        return self.marks + other.marks

s1=Student(50)
s2=Student(60)

print(s1+s2)


print('============================================Duck typing======================================================')

class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

def lets_fly(flyable_thing):
    flyable_thing.fly()

lets_fly(Bird())
lets_fly(Airplane())


print('============================================Polymorphism with Classes======================================================')

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

def area(shape):
    print("Area:", shape.area())

a1= Rectangle(5, 10)
a2= Circle(7)

area(a1)
area(a2)

print('========================================================Polymorphism with Inheritance (Method Overriding)=======================================')


