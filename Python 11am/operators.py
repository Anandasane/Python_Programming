# Arithmetic Operators
# 1. Addition Operator

a = 10
b = 34
print("Value of a:", a)
print("Value of b:", b)
print(f'the additon of the two integer number is: {a+b}')

# boolean variable addition

a = True
b = False
print('the value of two boolean addition is: ', a+b)
print('the value of logical OR is:', a or b)
print('the value of logical AND is:', a and b)
print('the value of logic is:', a and not b)

# floating value addition

a = 100.34
b = 322.432
print("Value of a:", a)
print("Value of b:", b)
print(f'the additon of the two float number is: {a+b}')


# store the answer in a variable
c = a+b
print("Stored addition result (c):", c)

# incremental and initializing at same time
c += 10
print(f'the incremental value by 10 is: {c}')

# 2. Subtraction Operator
a = 34
b = 23
print("Value of a:", a)
print("Value of b:", b)
print(f'the Substraction of the two number is: {a-b}')

c = a-b
print("Stored subtraction result (c):", c)

# decrementing and initializing at a same time
c -= 10
print(f'the decrement of the two number is: {c}')

# 3. Multiplication Operator
a = 10
b = 34
print("Value of a:", a)
print("Value of b:", b)
print(f'the multiplication of the two number is: {a*b}')

c = a*b
print("Stored multiplication result (c):", c)

# exponential incrementation and initializing at a same time
z = 2
z *= 2
print(f'the exponential increment by 2 is: {z}')

# 4. Division Operator (returns complete value after point)
a = 24
print("Value of a:", a)
b = 55
print("Value of b:", b)
print("Result of a / b:", a/b)
print("Result of b / a:", b/a)

c = a/b
print(f'the division of the two number is:{c}')

# decrementation and initializing at same time
z = 39
z /= 2
print(f'the decremental division value by 2 is :{z}')

# 4. floor division Operator (returns only the value not after the decimal)
print("Floor division of a // b:", a//b)
print("Current value of c:", c)
c = a//b
print("Stored floor division result (c):", c)
print(f'the floor division by 10 is :{c//10}')

z = 23
print("Value of z:", z)
z //= 10
print(f'the floor division by 10 is: {z}')

# 5. Percent Operator (returns the remainder of the division )
a = 24
print("Value of a:", a)
print(f'the remainder of the number by 10: {a%10}')

b = 355
print("Remainder of b % 10:", b%10)
print("Remainder of a % b:", a%b)

c = a%b
print("Stored modulo result (c):", c)

z = 34
z %= 10
print("Value of z after z %= 10:", z)

# Comparison Operator
a = 20
b = 3

print("When a=20 and b=3 -> Is a equal to b?:", a == b)
print("When a=20 and b=3 -> Is a greater than b?:", a > b)
print("When a=20 and b=3 -> Is a less than b?:", a < b)
print("When a=20 and b=3 -> Is a less than or equal to b?:", a <= b)
print("When a=20 and b=3 -> Is a greater than or equal to b?:", a >= b)

a = 100
b = 100
print("When a=100 and b=100 -> Is a equal to b?:", a == b)
print("When a=100 and b=100 -> Is a greater than b?:", a > b)
print("When a=100 and b=100 -> Is a less than b?:", a < b)
print("When a=100 and b=100 -> Is a less than or equal to b?:", a <= b)
print("When a=100 and b=100 -> Is a greater than or equal to b?:", a >= b)

a = 100
b = -1000
print("When a=100 and b=-1000 -> Is a equal to b?:", a == b)
print("When a=100 and b=-1000 -> Is a greater than b?:", a > b)
print("When a=100 and b=-1000 -> Is a less than b?:", a < b)
print("When a=100 and b=-1000 -> Is a less than or equal to b?:", a <= b)
print("When a=100 and b=-1000 -> Is a greater than or equal to b?:", a >= b)

a = 2
print(a**2)
