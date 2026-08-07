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

