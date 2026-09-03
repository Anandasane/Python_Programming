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