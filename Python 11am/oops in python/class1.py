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


