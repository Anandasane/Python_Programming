print('=============================================== Recursive Function ====================================')

def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)

print(factorial(4))


def add(a,b):
    return a+b

print(add(32,34))

def count_up(n):
    for i in range(n):
        yield i

a=count_up(5)
print(next(a))


def sum(a):
    if a==0:
        return 0
    return a + sum(a-1)

print(sum(100))


def febonacci(a):
    if a==1:
        return 1
    return febonaaci(a-1)+febonacci(a-2)+a

print(febonacci(5))


a=[-24,42,5,3,2,-5,5,-24,-54,-23]

def positive_number(a):   
    for i in range(len(a)): 
        if(a[i]>0):
             yield a[i] 
    

print(list(positive_number(a)))
    


