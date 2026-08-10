print('------------------list--------------------')

a=[21,24,22,53,23]

print(a)
print(a[2])

a[2]= 45
print(a[2])

a.append(34)
print(a)

print(len(a))

print(a.count(21))

print(a.index(45))

a.insert(2,22)

print(len(a))

a.sort()
print(a)

a.remove(22)
print(a)

a.pop(1)
print(a)

print(len(a))

b=[66,77,33,22,11]

a=a+b
print(a)

a.extend(b)
print(a)

# a.clear()
# print(a)

print(a.index(33))
print(a.count(33))

a.sort(reverse=True)
print(a)

[x**2 for x in range(10) if x % 2 == 0] 

s=[1,2,3,4,5,6]

for i in range(0,len(s)):
    print(s[i]*s[i])


d=['python',55,333,True,False,None]

e=[]
print(type(e))
print(e)

for i in range(0,len(d)):
    e.append(d[i])
    print(e)

print(e)

s=[10,39,33,[4,44,66,2,4,22],35,[6,77,0],56,43,321,45]
print(s[3][3])

print(s)



s=[34,43,53,5,73,23]
m=s[0]
for i in range(0,len(s)):
    if(s[i]<m):
        m=s[i]
    i+=1

print(m)

