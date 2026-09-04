print('==========================================================Multiple inheritance=====================================================')

class A:
   # propertys = 1000

   def land(self):
      propertys = 1000
      print(f"Class A inherited the vlaue is: {propertys}")


class B:
   propertys = 2000

   def land(self):
      A.land(self)
      print(f"Class B inherited the vlaue is: {self.propertys}")


class C(B,A):
   pass

c=C()
c.land()
