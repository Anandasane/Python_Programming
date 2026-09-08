print('===========================================polymorphism=====================================================')
print('===========================================overloading======================================================')

class Function:

    def add(self,a=0,b=0,c=0):
        print(a+b+c)
        print(2)

f=Function()
f.add(13,21)


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
