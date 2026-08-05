print('--------------------------------------------integer---------------------------------------------------')

a=10
print(type(a))

b=float(a)
print(type(b))

print(a)
print(b)

c=complex(a)
print(type(c))
print(c)

d=str(a)
print(type(d))
print(d)

e=bool(a)
print(type(e))
print(e)

f=bool(0)
print(type(f))
print(f)

# n=None(a)
# print(type(n))

print('------------------------------------------Float------------------------------------------------------')

a=45.4
print(type(a))
print(a)

b=int(a)
print(type(b))
print(b)

c=complex(a)
print(type(c))
print(c)

d=str(a)
print(type(d))
print(d)

e=bool(a)
print(type(e))
print(e)

f=bool(-56.5)
print(type(f))
print(f)

print('-----------------------------------------------Complex---------------------------------------------')


a=56+5j
print(type(a))

print(a)

a=53+5j
b=int(a)
print(type(b))
print(b)

a=53+5j
b=float(a)
print(type(b))
print(b)

# e=float(a)
# print(type(e))
# print(e)

a=53+5j
s=str(a)
print(type(s))
print(s)

#print(s.real)

g=bool(10+0j)
print(type(g))
print(g)

print('------------------------------------------String------------------------------------------------------------')

a='a'
print(type(a))
print(a)

# b=int(a)  error
# print(type(b))
# print(b)

# c=int('10.8')   error
# print(type(c))
# print(c)

d=float('10.8')
print(type(d))
print(d)

e=complex('10.5')
print(type(e))
print(e)

print(e.real)
print(e.imag)



f=bool(a)
print(type(f))
print(f)


e=bool('False')
print(type(e))
print(e)

g=bool('0')
print(type(g))
print(g)

# t=None('')
# print(type(t))
# print(t)

print('------------------------------------------boolean---------------------------------------------------')


a = True

b=int(a)
print(type(b))
print(b)

a = True
c=float(a)
print(type(c))
print(c)

d = False
e =int(d)
print(type(e))
print(e)


d=False
f=float(d)
print(type(f))
print(f)

a = True
g=complex(a)
print(type(g))
print(g)


a = False
h=complex(a)
print(type(h))
print(h)

print('------------------------------------------None---------------------------------------------------')

a = None
b=int(a)
print(type(b))
print(b)

a = None
b= float(a)
print(type(b))
print(b)

a = None
b= complex(a)
print(type(b))
print(b)

a=None
b=str(a)
print(type(b))
print(b)

