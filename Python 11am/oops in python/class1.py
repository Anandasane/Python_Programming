print('-------------------ooops classes ------------------------------------------------------------------------')

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
       s=input()
       print('changed student name is : ', s)




s=Student()
s.show()
s.show_rollno()

s.Entername('z')