print('===========================================overriding======================================================')
class A:
    def show(self):
        print("In A")

class B(A):
    def show(self):
        print("In B")

b=B()
b.show()

a=A()
a.show()