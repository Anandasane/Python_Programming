print('==========================================================Hybrid inheritance=====================================================')

print('==========================================================Multiple and hierarchical Hybrid inheritance=====================================================')

class A:
   def show(self):
      print('Class A method is called')


class B(A):
   def show(self):
      print('Class B method is called')


class C(A):
   def show(self):
      B.show(self)
      print('Class C method is called')


class D(B,C):
   def show(self):
      print('Class D method is called')
      super().show()


d=D()
d.show()
a=super(D,d)
a.show()
b=super(D,d)
b.show()
c=super(D,d)
c.show()
