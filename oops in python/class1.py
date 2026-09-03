print('-------------------------------------------------oops classes ----------------------------------------------------------------')

class Student:    
    name= 'chetan'
    rollno = 22
    age= 33
    occupation= "student"


    def show(self,):
      print("Student Name: ",Student.name)

    def show_rollno(self):
       print("Student Roll no is : ",Student.rollno)

    def Entername(name,self):
       #s=input()
       print('changed student name is : ',name)


s=Student()
s.show()
s.show_rollno()
s.Entername('z')

print(s.name)
print(s.age)

print('================================Bike class=========================================================')
class bike:
   name = "hayabusa"
   color='Red'
   price=999999

   def top_speed(self):
      print('Top speed is : 250')

   def show_details(self):
      print('Name of the bike: ',self.name,'\nPrice is :',self.price,'\ncolor: ',self.color)

   # default Constructor
   # def __init__(self):
   #    pass

   def __init__(self,name,color,price):
      print('it is a parameterized constructor ')
      self.name =name
      self.price=price
      self.color=color
      print(self.name,self.price,self.color)

   # No Argument constructor 
   # def __init__(self):
   #    print('constructor is called  when object is created ')
   #    self.price=12000
   #    self.color='Yellow'
   #    self.name='jawa'


b=bike('jawa','black',30000)
c=bike('a','b',2000)

print('============================Parameter constructor================================================')

class login:
   # user=''
   # password=''

   def show(self):
      print(self.user)
      print(self.password)


   def __init__(self,u,p):
      self.user=u
      self.password=p


ramesh=login('ramesh','123')
ramesh.show()
om=login('om','344')
om.show()

print('===================================Calculate class=================================================')


class cal:
   a=0
   b=0
   result=0

   def add(self):
      print(self.a+self.b)

   def sub(self):
      return  print(self.a-self.b)

   def mul(self):
      return print(self.a*self.b)

   def __init__(self):
      print('constructor called')
      print(self.a,self.b,self.result)

   def __init__(self,a,b):
      print('parametrized constructor is called')
      self.a=a
      self.b=b
      self.add()
      self.sub()
      self.mul()



a=cal(20,30)
a.add()
a.sub()
#print(a.sub())
multiple=a.mul()
print(multiple)

b=cal(10,20)
b.add()
b.sub()
b.mul()

print('=============================laptop class===========================================')

class laptop:
   def showdetails(self,name):
      n=500
      print(name)
      print(n,id(n))

   def show(self):
      self.n=700
      print(self.n)

   def __init__(self,p,c):
      self.price=p
      self.color=c


l=laptop(50000,'WHITE')
l.showdetails('HP')
l.show()

print('===============================================Static method====================================')

class Math:

   c = 49
   print('id of the class variable c: ',id(c))

   @staticmethod
   def add(a,b): # static Method
      print(a+b+Math.c)
      print('id of class variable using a object m: ',id(Math.c))
      print(a+b)


   def sub(self):# instance method
      self.a=20
      print(self.a)
      print('id of instance variable: ',id(self.a))

   def __init__(self):
      self.x=20
      self.y=35

m=Math()
print(m.sub())
Math.add(10,15)



print('============================using decorator===========================================')
def dec(f):
      def wrap(self,u,p): # parameter must be same
         print('Login start')
         f(self,u,p)    # parameter must as of wrap function
         print('Login End')
      return wrap

class login:
   # def dec(f):
   #    def wrap(self,u,p):
   #       print('Login start')
   #       f(self,u,p)
   #       print('Login End')
   #    return wrap

   @dec
   def userlogin(self,u,p):
      if(u=='abc'and p=='123'):
         print('Login success')
      else:
         print('Invalid Login')

l=login()
l.userlogin('abc','123')
l.userlogin(p='123',u='abc')

print('===============================================Encapsulation================================================')

class bank:
   __bank=1242

   def showbal(self,p):
      if(p==1234):
         return 'Bank balance is : ',self.__bank
      else:
         return 'wrong pin'

b=bank()
p=int(input('Enter pin: '))
print(b.showbal(p))
# print(b.showbal(1234))

print('=========================================BANK CLASS ENCAPSULATION==========================================')

class Bank:
   __bal=10000

   def showbal(self):
      p=int(input('Enter a pin:'))
      if(p==1234):
         return f'Bank balance is :{self.__bal}'
      else:
         return 'wrong pin'

   def deposit(self,amount):
      p=int(input('Enter a pin:'))
      if(p==1234):
         self.__bal+=amount
         return 'Amount deposited successfully'
      else:
         return 'wrong pin'

   def withdraw(self,amount):
      p=int(input('Enter a pin:'))
      if(p==1234):
         if(amount>self.__bal):
            return 'Insufficient balance'
         else:
            self.__bal-=amount
            return 'Amount withdrawn successfully'
      else:
         return 'wrong pin'

b=Bank()
print(b.showbal())
print(b.deposit(200))
print(b.withdraw(100))
print(b.showbal())

print('====================================ATM using single level inheritance ============================')

class Bank:
   __bal=10000

   def showbal(self):
      p=int(input('Enter a pin:'))
      if(p==1234):
         return f'Bank balance is :{self.__bal}'
      else:
         return 'wrong pin'

   def deposit(self,amount):
      p=int(input('Enter a pin:'))
      if(p==1234):
         self.__bal+=amount
         return 'Amount deposited successfully'
      else:
         return 'wrong pin'

   def withdraw(self,amount):
      p=int(input('Enter a pin:'))
      if(p==1234):
         if(amount>self.__bal):
            return 'Insufficient balance'
         else:
            self.__bal-=amount
            return 'Amount withdrawn successfully'
      else:
         return 'wrong pin'


class ATM(Bank):
   def check_pin(self):
      p=int(input('Enter a pin:'))
      if(p==1234):
         return 'Pin is correct'
      else:
         return 'wrong pin'
   
   def showbal(self):
      return super().showbal()

   def deposit(self,amount):
      return super().deposit(amount)

   def withdraw(self,amount):
      return super().withdraw(amount)
   
b=Bank()
a=ATM()

print(b.showbal())

print('=================================heirarchyical inheritance==================================')


class Bank:
   location= 'nagar'

   def ifscc(self):
      print('barbo1234')


class acc1(Bank):
   name='raju'
   def showbal(self):
      print(f'Bank balance of {self.name} is : 10000')
      super().ifscc()

class acc2(Bank):
   name='om'
   def showbal(self):
      print(f'Bank balance of {self.name} is : 20000')
      super().ifscc()


ac1=acc1()
ac2=acc2()

ac1.name
ac1.showbal()
ac1.location

ac2.name
ac2.showbal()
ac2.location
   

