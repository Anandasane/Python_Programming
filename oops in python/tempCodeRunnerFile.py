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