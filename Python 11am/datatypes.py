# integer datatype
a=20
b=49
c=20

print(a)
print(type(a))
print(id(a))

print(b)
print(type(b))
print(id(b))

print(c)
print(type(c))
print(id(c))

# declaring multiple varaible same value at a time

a=b=c = 49
print(a,b,c)
print(type(a),type(b),type(c))
print(id(a),id(b),id(c))

# declaring multiple varaible different value at a time
a,b,c = 12,34,65
print(a,b,c)
print(type(a),type(b),type(c))
print(id(a),id(b),id(c))

# declearing complex number
# use alphabet j only for imaginary part 
a = 4+5j
print(a)
print(a.real)
print(a.imag)

# differnt method to declar complex number using complex function
a = complex(4,5)
print(a)
print(a.real)
print(a.imag)

#String data type
#declaring string
a= 'abc'
print(a)
print(type(a))

b="ABC"
print(b)
print(type(b))

c='10'
d='20'

x=10
y=30
print(x+y)
print(c+d)

a='python'
print(a[0])
print(a[1])

p="In Python, a string is a sequence of character enclosed"
print(p[-1])
print(p[-2])

r='Hello Python0689698408rgkjkgs;'
print(r[5])
print(r[6])

#Boolean data type
a=True
print(a)
print(type(a))

b='False'
print(b)
print(type(b))

c='true'
print(c)
#None data type
a = None
print(a)
print(type(a))
print(10)

print(100/3)
print(100//3)

print(2**10)

a=int(input("enter any datatype value:"))
print(type(a))

