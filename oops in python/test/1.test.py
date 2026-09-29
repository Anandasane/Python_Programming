print("========================================= Class =====================================================")

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

    def display(self):
        print(f"Name of the Student is {self.name}")
        print(f"Marks of the student is {self.marks}")


s=Student('tushar',98)
s.display()
s=Student('shubham',27)
s.display()

print('=================================== Question 2 =====================================')

class Employee:
    def __init__(self,id,name,department,salary):
        self.id=id
        self.name=name
        self.department=department
        self.salary = salary

    def display(self):
        print(f"The Id of the Employee is {self.id}")
        print(f"The Name of the Employee is {self.name}")
        print(f"The department of the Employee is {self.department}")
        print(f"The salary of the Employee is {self.salary}")



e=Employee(23,'shubham','HR',30000)
e.display()
e=Employee(45,'Tushar','Data Manager',500000)
e.display()

print('=================================================== Question 3 =========================================================')

class BankAccount:
    def __init__(self,account_no,holder_name,balance):
        self.account_no=account_no
        self.holder_name=holder_name
        self.balance=balance

    def display(self):    
        print(f"The account number is {self.account_no}")
        print(f"The Name of Account Holder is {self.holder_name}")
        print(f"The Account Blance is {self.balance}")

b=BankAccount(123,'Anand',400000)
b.display()
b=BankAccount(344,"chetan",200000)
b.display()

print('=================================================== Question 4 =========================================================')

class Product:
    def __init__(self,p_id,name,price):
        self.p_id=p_id
        self.name=name
        self.price=price

    def display(self):
        print(f"The Product Id is {self.p_id}")
        print(f"The Name of the Product is {self.name}")
        print(f"The Price of the Product is {self.price}")


p=Product(23,'laptop',45000)
p.display()
p=Product(45,'Mobile',20000)
p.display()

print('=================================================== Question 5 =========================================================')

class Laptop:
    def __init__(self,brand,RAM,processor,price):
        self.brand=brand
        self.RAM=RAM
        self.processor=processor
        self.price=price

    def display(self):
        print(f"the Brand of the Laptop is {self.brand}")
        print(f"the RAM of the Laptop is {self.RAM}")
        print(f"The processor of laptop is {self.processor}")
        print(f"the Price of the Laptop is {self.price}")


l=Laptop("HP",16,"intel",45000)
l.display()
l=Laptop('dell',8,"AMD",40000)
l.display()

print("=============================================================== Instance Method ====================================================================")

print("====================================================================== Question 1 ===========================================================================")

class Student:
    name="Anand"
    roll_no=12
    marks=98
    course="Data analyst"
    percentage=89

    def display(self):
        print("this is an istance method")
        print(f"The name of the Student is {self.name}")
        print(f"The Roll No of the Student is {self.roll_no}")
        print(f"The Marks of the Student is {self.marks}")
        print(f"The Course of the Student is {self.course}")

    def percetange(self):
        
        print("this is a percentage instance method")
        print(f"The percentage of the Student is {self.percentage}%")


s=Student()
s.display()
s.percetange()

print("====================================================================== Question 2 ===========================================================================")

class Rectangle:

    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        print(f"The Area of the Rectangle is {self.length * self.breadth}")

    def perimeter(self):
        print(f"The Perimeter of the Rectangle is {2*self.length + 2*self.breadth}")


r=Rectangle(5,10)
r.area()
r.perimeter()

print("====================================================================== Question 3 ===========================================================================")

class BankAccount:
    balance=1000
    print(f"The current Account Balance is {balance}")

    def deposite(self,amount):
        self.amount=amount
        self.balance= self.balance + amount
        print(f"The Balance after deposite is {self.balance}")

    def withdraw(self,amount):
        self.amount=amount
        self.balance=self.balance - amount
        print(f"The Balance after withdraw is {self.balance}")


b=BankAccount()
b.deposite(500)
b.withdraw(100)
print('The Final Balance is: ',b.balance)

print("====================================================================== Question 4 ===========================================================================")

class Employee:
    emp1=200000
    emp2=300000
    emp3=400000

    def annual_salary(self):
        print(f"The Annual Salary of the employees is {self.emp1 + self.emp2 + self.emp3}")



e=Employee()
e.annual_salary()

print("====================================================================== Question 5 ===========================================================================")


class Circle:

    def calculate_Area(self,radius):
        self.radius=radius
        print(f"The Area of the Circle is: {(self.radius*self.radius) *3.14}")


c=Circle()
c.calculate_Area(5)

print('=================================================================== Encapsulation =============================================================================')

print('==================================================================== Question 1 ================================================================================')

class BankAccount:
    __balance=1000
    print(f"The current Account Balance is {__balance}")


    def deposite(self,amount):
        self.amount=amount
        self.__balance= self.__balance + amount
        print(f"The Balance after deposite is {self.__balance}")

    def withdraw(self,amount):
        self.amount=amount
        self.__balance=self.__balance - amount
        print(f"The Balance after withdraw is {self.__balance}")


b=BankAccount()
b.deposite(500)
b.withdraw(100)
# print('The Final Balance is: ',b.__balance)

print('=========== Question 2 ===========')

class Student:
    __marks = 77                     

    @property                       
    def marks(self):
        return self.__marks

    @marks.setter                    
    def marks(self, m):
        self.__marks = m             
        print(f"The new Marks after setter is: {m}")


s = Student()
print(s.marks)     

s.marks = 90        
print(s.marks)      

print('==================================================== Question 3 ==========================================================')

class Employee:
    __salary = 20000

    
    def get_salary(self):
        return  self.__salary


    
    def set_salary(self,amount):
        self.__salary=amount
        print(f"The new Salary is: {amount}")

e=Employee()
print(e.get_salary())

e.set_salary(99000)
print(e.get_salary())


print('=============================================================== Question 4 ===========================================================')

class Mobile:
    __price=2000

    def set_price(self,amount):
        self.amount = amount
        if(amount>self.__price):
            self.__price=amount
            print(f"The new Price for Mobile is {self.__price}")
        else:
            print("new  price must be greater than original try again")

    def get_price(self):
        return self.__price

m=Mobile()
print(m.get_price())

m.set_price(40000)
print(m.get_price())

m.set_price(20000)
print(m.get_price())

class Password:
    __password=123

    def set_password(self,np):
        self.np=np
        if(np:=(int(input("Enter new password"))) == self.__password):
            self.__password = np
            print("New password is set successfully ")
        else:
            print("Enter the right password Try again")

    def get_password(self):
        return f'The new password is {self.__password}'
    
p=Password()
p.get_password()

p.set_password()
p.get_password
