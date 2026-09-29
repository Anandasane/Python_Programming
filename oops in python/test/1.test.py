print('================================Question 1==========================================================')


class Student:
    name="Anand"
    age = 22
    course="Data Science"


s=Student()
print(s.name)
print(s.age)
print(s.course)
print(s.name,s.age.s.course)


print('============================== Question 2===================================================')

class Car:
    def display(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        print(f"{self.brand} car with model {self.model} and pCrice {self.price}")


c=Car()
d=Car()
c.display("bmw",'m5',20000000)
d.display('audi','m6',30000000)

print('=============================== Question 3 ========================================')

class Employee:
    def display(self,ID,name,salary):
        self.ID=ID
        self.name=name
        self.salary=salary
        print(f"employee id is {self.ID} and employee name is {self.name} and salary is {self.salary} ")

e=Employee()
e.display('12200','parasd',2000000)


print('====================================== Question 4 ==========================================')

class Book:
    def show(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
        print(f"{self.title} book with author {self.author} and price {self.price}")


a=Book()
b=Book()
c=Book()
d=Book()
e=Book()

a.show('bhagvat gita', 'krishna',200)
b.show("harry potter",'harry',2000)
c.show('english book','english sir',2300)
d.show('math book', 'math sir',400)
e.show('history book', 'history sir', 300)

print('=================================== Question 5 ==========================================')

class Mobile:
    company_name='Nokia'
    model='lava'
    price=800

m=Mobile()
print(m.company_name,m.model,m.price)

print('=================================== Constructor =========================================')
print('=================================== Question 1 ==========================================')

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print(f"Name of the Student is {self.name}")
        print(f"Marks of the student is {self.marks}")


s=Student('tushar',98)
s=Student('shubham',27)

print('=================================== Question 2 =====================================')

class Employee:
    def __init__(self,id,name,department,salary):
        self.id=id
        self.name=name
        self.department=department
        self.salary = salary
        print(f"The Id of the Employee is {self.id}")
        print(f"The Name of the Employee is {self.name}")
        print(f"The department of the Employee is {self.department}")
        print(f"The salary of the Employee is {self.salary}")



e=Employee(23,'shubham','HR',30000)
e=Employee(45,'Tushar','Data Manager',500000)


