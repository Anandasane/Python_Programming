print('_-------------------------------list----------------------------------------')

# list is an ordered , mutable collection of items.

numbers=[21,24,22,53,23,22,44,53,63]
names=['anand','chetan','sachin','rohit']
mixed=[21,'anand',True,22.5]


print(len(mixed))
print(type(mixed))

print(numbers[2])
print(names[1])
print(mixed[0])

numbers.append(34)
print(numbers)

numbers.insert(2,22)
print(numbers)

numbers.remove(22)
print(numbers)

numbers.pop() 
print(numbers)

numbers.pop(1)
print(numbers)

print(numbers.index(53))

print(numbers.count(22))

print(numbers.sort())

print(numbers.sort(reverse=True))

no=numbers.copy()
print(no)

print(numbers[3:4])
print(numbers[2:5])
print(numbers[::])

print(33 in numbers)

print(30 in numbers)

print(22 not in numbers)

squares=[x**2 for x in range(10) if x % 2 == 0]
print(squares)

L=[1,2,3,4,5,6,[7,8,9],[10,11,12]]
print(L[6][1])

print(min(numbers))
print(max(numbers))
print(sum(numbers))


numbers.clear()
print(numbers)

print('_-------------------------------tuple----------------------------------------')

# A tuple is an ordered , immutable collection of items.

t=(21,24,22,53,23,22,44,53,63)
print(t)

t2=(22,)
print(t2)

print(t[2])
print(t[-1])

print(t[2:5])
print(t[::])

for i in t:
    print(i)

print(len(t))

print(t.count(33))

print(t.index(24))

print(23 in t)
print(33 not in t)

t1=34,53,23,65

a,g,s,c=t1

print(a,g,s,c)

t3=t1+t2
print(t3)
print(t2*3)

t4=((33,34),(55,32))

print(min(t1))
print(max(t1))
print(sum(t1))

lst=[23,24,12,44,24]
t5=tuple(lst)

# Why Use Tuple?

# ✔️ Faster than list
# ✔️ Data safety (cannot change)
# ✔️ Used for fixed data

print('---------------------------set-------------------------------------')

s1={2,14,23,12,3,33}
s2=set([3,42,21,5])

print(s1)
print(s2)

s=set()
print(s)
s.add(4)
print(s)

s.update([23,2,4,12])
print(s)

s.remove(23)
print(s)

s.discard(5)
print(s)
s.pop()
print(s)
s.clear()
print(s)

s={3,4,1,44}
print(len(s))

s={34,33,22,11,35}

print(33 in s)
print(34 not in s)

a={1,2,3}
b={3,4,5}

print(a|b)
print(a.union(b))

print(a & b)
print(a.intersection(b))

print(a-b)
print(b-a)

print(a^b)
print(a.symmetric_difference(b))

a={1,2}
b={1,2,3}

print(a.issubset(b))
print(b.issuperset(a))

a={1,2}
b={3,4}

print(a.isdisjoint(b))

a={1,2,3}
b=a.copy()

# cannot add or remove element
fs=frozenset([1,2,4])

# loop throught the set
s={12,34,1,2}
for i in s:
    print(i)

# Remove Duplicate using set
lst=[1,2,3,4,2,3]

unique=list(set(lst))
print(unique)

fs=frozenset([2,2,1,4,3,4,3])
print(fs)

# What You CANNOT Do with Frozenset 
# fs.add(4)        #  Error
# fs.remove(2)     #  Error
# fs.update([5])   #  Error

a=frozenset([1,2])
b=frozenset([2,3])

print(a|b)
print(a.union(b))

print(a & b)
print(a.intersection(b))

print(a-b)
print(a.difference(b))

print(a^b)
print(a.symmetric_difference(b))

a = frozenset([1, 2])
b = frozenset([1, 2, 3])

print(a.issubset(b))
print(b.issuperset(a))

# Frozenset as dictionary 
permissions = {
    frozenset(["read", "write"]): "Admin",
    frozenset(["read"]): "User"
}

# convert set to frozenset

s={1,23,4}
fs=frozenset(s)
print(fs)
s=set(fs)
print(s)

print('-------------------------dictionary--------------------------')

# dictionary stores data in key value pairs
# keys are unique
# values can be duplicate
# unordered (insertion order preserved from python 3.7+)

student={
    'id':122,
    'name':"anand".capitalize(),
    'marks':99,
    'rollno':23,
    'course':'data analytics'
}

print(student)

d1={'a':1,'b':2,'c':3}
print(d1)

d2=dict(name="ram", age=33,rollno=34)
print(d2)
# empty dictionary
d={}
print(d)

# accessing dictionary values
print(student['name'])
print(student.get('marks'))
print(student.get('grade','not found'))

# add or update elements
student['age']=22
student['marks']=90
print(student)
# remove elements

student.pop('marks')
print(student)
#remove last item
student.popitem()
print(student)

# using del keyword
del student['rollno']
print(student)

# print key values and items in dictionary
print(student.items())
print(student.keys())
print(student.values())

# prints length of the dictionary
print(len(student))

# loop through dictonary keys

for k in student:
    print(k)

# loop through dictionary values

for v in student.values():
    print(v)

# loop throught dictionary keys and values

for k,v in student.items():
    print(k,v)


# check key exists
print('name'in student)

print('salary'in student)

# copy dictionary
d2=student.copy

# update merge dictionaries
d1={"a":1}
d2={'b':2}

d1.update(d2)
print(d1)

# from keys()
keys=['id','name','age']
d=dict.fromkeys(keys,None)
print(d)

# Nested dictionary

Student={
    'Name':'Rahul',
    "marks":{"math":39,"science":35}

}

print(Student)



# clear remove all items
student.clear()
print(student)


