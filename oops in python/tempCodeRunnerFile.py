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
