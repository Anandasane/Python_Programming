print('================================Question 1==========================================================')

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(f"The name of the Student is {self.name}")
        print(f"The age of the Student is {self.age}")
        print(f"The course of the Student is {self.course}")


s1 = Student("Anand", 22, "Data Science")
s1.display()
s2 = Student("Tushar", 23, "AI")
s2.display()
s3 = Student("Shubham", 21, "ML")
s3.display()


print('============================== Question 2 ===================================================')

class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print(f"{self.brand} car with model {self.model} and price {self.price}")


c = Car("BMW", "M5", 20000000)
d = Car("Audi", "M6", 30000000)
c.display()
d.display()


print('=============================== Question 3 ========================================')

class Employee:
    def __init__(self, ID, name, salary):
        self.ID = ID
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Employee id is {self.ID} and employee name is {self.name} and salary is {self.salary}")


e = Employee(12200, "Parasd", 2000000)
e.display()


print('====================================== Question 4 ==========================================')

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show(self):
        print(f"{self.title} book with author {self.author} and price {self.price}")


a = Book("Bhagwat Gita", "Krishna", 200)
b = Book("Harry Potter", "Rowling", 2000)
c = Book("English Book", "English Sir", 2300)
d = Book("Math Book", "Math Sir", 400)
e = Book("History Book", "History Sir", 300)

a.show()
b.show()
c.show()
d.show()
e.show()


print('=================================== Question 5 ==========================================')

class Mobile:
    def __init__(self, company_name, model, price):
        self.company_name = company_name
        self.model = model
        self.price = price

    def display(self):
        print(f"The company is {self.company_name}, model is {self.model} and price is {self.price}")


m = Mobile("Nokia", "Lava", 800)
m.display()


print('=================================== Constructor =========================================')

print('=================================== Question 1 ==========================================')

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name of the Student is {self.name}")
        print(f"Marks of the student is {self.marks}")


s = Student("tushar", 98)
s.display()
s = Student("shubham", 27)
s.display()


print('=================================== Question 2 =====================================')

class Employee:
    def __init__(self, id, name, department, salary):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print(f"The Id of the Employee is {self.id}")
        print(f"The Name of the Employee is {self.name}")
        print(f"The department of the Employee is {self.department}")
        print(f"The salary of the Employee is {self.salary}")


e = Employee(23, "shubham", "HR", 30000)
e.display()
e = Employee(45, "Tushar", "Data Manager", 500000)
e.display()


print('=================================================== Question 3 =========================================================')

class BankAccount:
    def __init__(self, account_no, holder_name, balance):
        self.account_no = account_no
        self.holder_name = holder_name
        self.balance = balance

    def display(self):
        print(f"The account number is {self.account_no}")
        print(f"The Name of Account Holder is {self.holder_name}")
        print(f"The Account Balance is {self.balance}")


b = BankAccount(123, "Anand", 400000)
b.display()
b = BankAccount(344, "chetan", 200000)
b.display()


print('=================================================== Question 4 =========================================================')

class Product:
    def __init__(self, p_id, name, price):
        self.p_id = p_id
        self.name = name
        self.price = price

    def display(self):
        print(f"The Product Id is {self.p_id}")
        print(f"The Name of the Product is {self.name}")
        print(f"The Price of the Product is {self.price}")


p = Product(23, "laptop", 45000)
p.display()
p = Product(45, "Mobile", 20000)
p.display()


print('=================================================== Question 5 =========================================================')

class Laptop:
    def __init__(self, brand, RAM, processor, price):
        self.brand = brand
        self.RAM = RAM
        self.processor = processor
        self.price = price

    def display(self):
        print(f"The Brand of the Laptop is {self.brand}")
        print(f"The RAM of the Laptop is {self.RAM}")
        print(f"The processor of laptop is {self.processor}")
        print(f"The Price of the Laptop is {self.price}")


l = Laptop("HP", 16, "intel", 45000)
l.display()
l = Laptop("dell", 8, "AMD", 40000)
l.display()


print("=============================================================== Instance Method ====================================================================")

print("====================================================================== Question 1 ===========================================================================")

class Student:
    def __init__(self, name, roll_no, marks, total):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        self.total = total

    def display(self):
        print("this is an instance method")
        print(f"The name of the Student is {self.name}")
        print(f"The Roll No of the Student is {self.roll_no}")
        print(f"The Marks of the Student is {self.marks}")

    def percentage(self):
        print("this is a percentage instance method")
        print(f"The percentage of the Student is {(self.marks / self.total) * 100}%")


s = Student("Anand", 12, 98, 100)
s.display()
s.percentage()


print("====================================================================== Question 2 ===========================================================================")

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print(f"The Area of the Rectangle is {self.length * self.breadth}")

    def perimeter(self):
        print(f"The Perimeter of the Rectangle is {2 * self.length + 2 * self.breadth}")


r = Rectangle(5, 10)
r.area()
r.perimeter()


print("====================================================================== Question 3 ===========================================================================")

class BankAccount:
    def __init__(self, balance=1000):
        self.balance = balance
        print(f"The current Account Balance is {self.balance}")

    def deposite(self, amount):
        self.balance = self.balance + amount
        print(f"The Balance after deposite is {self.balance}")

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(f"The Balance after withdraw is {self.balance}")


b = BankAccount()
b.deposite(500)
b.withdraw(100)
print("The Final Balance is: ", b.balance)


print("====================================================================== Question 4 ===========================================================================")

class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        print(f"The Annual Salary of {self.name} is {self.monthly_salary * 12}")


e = Employee("Anand", 200000)
e.annual_salary()
e = Employee("Tushar", 300000)
e.annual_salary()


print("====================================================================== Question 5 ===========================================================================")

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_Area(self):
        print(f"The Area of the Circle is: {3.14 * self.radius * self.radius}")

    def calculate_Circumference(self):
        print(f"The Circumference of the Circle is: {2 * 3.14 * self.radius}")


c = Circle(5)
c.calculate_Area()
c.calculate_Circumference()


print('=================================================================== Encapsulation =============================================================================')

print('==================================================================== Question 1 ================================================================================')

class BankAccount:
    def __init__(self):
        self.__balance = 1000
        print(f"The current Account Balance is {self.__balance}")

    def deposite(self, amount):
        self.__balance = self.__balance + amount
        print(f"The Balance after deposite is {self.__balance}")

    def withdraw(self, amount):
        self.__balance = self.__balance - amount
        print(f"The Balance after withdraw is {self.__balance}")

    def get_balance(self):
        return self.__balance


b = BankAccount()
b.deposite(500)
b.withdraw(100)
# print(b.__balance)   # AttributeError -> private
print("The Final Balance is: ", b.get_balance())


print('==================================================================== Question 2 ================================================================================')

class Student:
    def __init__(self):
        self.__marks = 77

    def set_marks(self, m):
        self.__marks = m
        print(f"The new Marks after setter is: {self.__marks}")

    def get_marks(self):
        return self.__marks


s = Student()
print("Marks are:", s.get_marks())
s.set_marks(95)
print("Marks are:", s.get_marks())


print('==================================================================== Question 3 ================================================================================')

class Employee:
    def __init__(self):
        self.__salary = 20000

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, amount):
        self.__salary = amount
        print(f"The new Salary is: {self.__salary}")


e = Employee()
print(e.salary)
e.salary = 99000
print(e.salary)


print('==================================================================== Question 4 ================================================================================')

class Mobile:
    def __init__(self):
        self.__price = 15000

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, amount):
        if amount <= 0:
            print("Invalid price")
        else:
            self.__price = amount
            print(f"The new Price is: {self.__price}")


m = Mobile()
print(m.price)
m.price = 25000
print(m.price)
m.price = -500


print('==================================================================== Question 5 ================================================================================')

class Password:
    def __init__(self, password):
        self.__password = password

    def verify(self, attempt):
        if attempt == self.__password:
            print("Password is Correct")
        else:
            print("Password is Wrong")


p = Password("anand123")
p.verify("anand123")
p.verify("wrongpass")


print('=================================================================== Inheritance =============================================================================')

print('==================================================================== Question 1 ================================================================================')

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")


d = Dog()
d.eat()
d.bark()


print('==================================================================== Question 2 ================================================================================')

class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")


c = Car()
c.move()
c.drive()


print('==================================================================== Question 3 ================================================================================')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name is {self.name} and Age is {self.age}")

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display(self):
        super().display()
        print(f"Course is {self.course}")


s = Student("Anand", 22, "Data Science")
s.display()


print('==================================================================== Question 4 ================================================================================')

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"Name is {self.name} and Salary is {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, team):
        super().__init__(name, salary)
        self.team = team

    def show(self):
        super().show()
        print(f"Team size is {self.team}")


m = Manager("Anand", 120000, 8)
m.show()


print('==================================================================== Question 5 ================================================================================')

class Shape:
    def describe(self):
        print("This is a shape")

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print(f"Area is {self.length * self.breadth}")


r = Rectangle(6, 4)
r.describe()
r.area()


print('=============================================================== Multilevel Inheritance ===============================================================')

print('==================================================================== Question 1 ================================================================================')

class Person:
    def __init__(self, name):
        self.name = name

    def who(self):
        print(f"Person name is {self.name}")

class Employee(Person):
    def __init__(self, name, eid):
        super().__init__(name)
        self.eid = eid

    def who(self):
        print(f"Employee {self.name} with id {self.eid}")

class Manager(Employee):
    def __init__(self, name, eid, bonus):
        super().__init__(name, eid)
        self.bonus = bonus

    def who(self):
        print(f"Manager {self.name} [{self.eid}] bonus {self.bonus}")


m = Manager("Sita", "M01", 50000)
m.who()


print('==================================================================== Question 2 ================================================================================')

class Animal:
    def breathe(self):
        print("Animal breathes")

class Mammal(Animal):
    def feed(self):
        print("Mammal feeds milk")

class Dog(Mammal):
    def speak(self):
        print("Dog barks")


d = Dog()
d.breathe()
d.feed()
d.speak()


print('==================================================================== Question 3 ================================================================================')

class Vehicle:
    def move(self):
        print("Vehicle moves")

class Car(Vehicle):
    def drive(self):
        print("Car drives")

class ElectricCar(Car):
    def charge(self):
        print("Electric car charges")


ec = ElectricCar()
ec.move()
ec.drive()
ec.charge()


print('==================================================================== Question 4 ================================================================================')

class Student:
    def study(self):
        print("Student studies")

class GraduateStudent(Student):
    def degree(self):
        print("Graduate student has degree")

class PhDStudent(GraduateStudent):
    def research(self):
        print("PhD student does research")


p = PhDStudent()
p.study()
p.degree()
p.research()


print('==================================================================== Question 5 ================================================================================')

class Device:
    def switch_on(self):
        print("Device switched on")

class Computer(Device):
    def process(self):
        print("Computer processes data")

class Laptop(Computer):
    def portable(self):
        print("Laptop is portable")


l = Laptop()
l.switch_on()
l.process()
l.portable()


print('=============================================================== Multiple Inheritance ===============================================================')

print('==================================================================== Question 1 ================================================================================')

class Father:
    def skill(self):
        print("Father skill is coding")

class Mother:
    def skill(self):
        print("Mother skill is cooking")

class Child(Father, Mother):
    pass


c = Child()
c.skill()   # Father's skill (MRO order)


print('==================================================================== Question 2 ================================================================================')

class Teacher:
    def teach(self):
        print("Teaching students")


class Researcher:
    def research(self):
        print("Doing research")

class Professor(Teacher, Researcher):
    def summary(self):
        self.teach()
        self.research()


p = Professor()
p.summary()


print('==================================================================== Question 3 ================================================================================')

class Engine:
    def start_engine(self):
        print("Engine is running")

class Battery:
    def charge(self):
        print("Battery is charged")

class ElectricCar(Engine, Battery):
    def status(self):
        self.start_engine()
        self.charge()


ec = ElectricCar()
ec.status()


print('==================================================================== Question 4 ================================================================================')

class Writer:
    def write(self):
        print("Writing the book")

class Editor:
    def edit(self):
        print("Editing the book")

class Author(Writer, Editor):
    def workflow(self):
        self.write()
        self.edit()
        print("Book published")


a = Author()
a.workflow()


print('==================================================================== Question 5 ================================================================================')

class Developer:
    def code(self):
        print("Writing code")

class Designer:
    def design(self):
        print("Designing UI")

class WebDeveloper(Developer, Designer):
    def build(self):
        self.design()
        self.code()
        print("Website is ready")


w = WebDeveloper()
w.build()


print('=========================================================== Method Overriding / Polymorphism ===========================================================')

print('==================================================================== Question 1 ================================================================================')

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")


for a in (Animal(), Dog(), Cat()):
    a.sound()


print('==================================================================== Question 2 ================================================================================')

class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def start(self):
        print("Car engine starts")

class Bike(Vehicle):
    def start(self):
        print("Bike kick start")


for v in (Car(), Bike()):
    v.start()


print('==================================================================== Question 3 ================================================================================')

class Employee:
    def work(self):
        print("Employee is working")

class Manager(Employee):
    def work(self):
        print("Manager manages team")

class Developer(Employee):
    def work(self):
        print("Developer develops software")


for e in (Manager(), Developer()):
    e.work()


print('==================================================================== Question 4 ================================================================================')

class Shape:
    def area(self):
        print("Area of shape")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Area of Circle is {3.14 * self.radius * self.radius}")

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print(f"Area of Rectangle is {self.length * self.breadth}")


for sh in (Circle(5), Rectangle(4, 6)):
    sh.area()


print('==================================================================== Question 5 ================================================================================')

class Payment:
    def pay(self, amount):
        print(f"Paying amount {amount}")

class UPIPayment(Payment):
        def pay(self, amount):
            print(f"UPI payment of {amount} is successful")

class CardPayment(Payment):
    def pay(self, amount):
        print(f"Card payment of {amount} is successful")


for p in (UPIPayment(), CardPayment()):
    p.pay(500)


print('=================================================================== Abstraction =============================================================================')

print('==================================================================== Question 1 ================================================================================')

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Area of Circle is {3.14 * self.radius * self.radius}")


# s = Shape()   # TypeError: Can't instantiate abstract class
c = Circle(5)
c.area()


print('==================================================================== Question 2 ================================================================================')

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started with ignition")


v = Car()
v.start()


print('==================================================================== Question 3 ================================================================================')

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        print(f"{amount} paid using UPI")

class Card(Payment):
    def pay(self, amount):
        print(f"{amount} paid using Card")


for p in (UPI(), Card()):
    p.pay(1000)


print('==================================================================== Question 4 ================================================================================')

class Employee(ABC):
    def __init__(self, name, basic):
        self.name = name
        self.basic = basic

    @abstractmethod
    def calculate_salary(self):
        pass

class Developer(Employee):
    def calculate_salary(self):
        print(f"{self.name} salary is {self.basic * 1.2}")

class Manager(Employee):
    def calculate_salary(self):
        print(f"{self.name} salary is {self.basic * 1.5}")


d = Developer("Anand", 50000)
d.calculate_salary()
m = Manager("Tushar", 60000)
m.calculate_salary()


print('==================================================================== Question 5 ================================================================================')

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")


for a in (Dog(), Cat()):
    a.sound()

print('========================================= ALL 9 SECTIONS COMPLETED =========================================')
