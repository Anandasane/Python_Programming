a=[10,35,24,66,43,33,65]
val=int(input('Enter the value you want to insert: '))
pos=int(input('Enter the position you want to insert the value in: '))

print(a)

a[pos:pos]=[val]
print(a)
