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
   def __init__(self):
      pass
   # No Argument constructor 
   def __init__(self):
      print('constructor is called  when object is created ')
      self.price=12000
      self.color='Yellow'
      self.name='jawa'


b=bike()
c=bike()
b.top_speed()
b.show_details()
print(b.color)


