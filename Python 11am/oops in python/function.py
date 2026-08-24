print('=======================================Lamda Function=====================================================')

a=int(input('Enter first number: '))
b=int(input('Enter second number: '))

add = lambda a,b:a+b
sub = lambda a,b:a-b
mul = lambda a,b:a*b
square = lambda a:a*a
divison = lambda a,b:a/b
mod = lambda a,b:a//b


print('addition of the numbers is ',add(a,b))
print('substraction of the numbers is ',sub(a,b))
print('mulitplication of the numbers is ',mul(a,b))
print('Square of the numbers is ',square(a))
print('divison of the numbers is ',divison(a,b))
print('modulus of the numbers is ',mod(a,b))

print('====================================================check lambda function==================================================')

even_odd = lambda a: "EVEN" if a % 2 == 0 else "ODD"
a = int(input('Enter a number: '))
print(even_odd(a))

is_prime = lambda n:"Prime" if n > 1 and not any(n % i == 0 for i in range(2, int(n**0.5) + 1)) else "Not Prime"
a = int(input('Enter a number: '))
print(is_prime(a))


n=int(input("Enter a number: "))

is_zero = lambda n: n == 0
is_positive = lambda n: n > 0
is_negative = lambda n: n < 0

is_perfect_square = lambda n: n >= 0 and int(n**0.5) ** 2 == n


print(is_zero(n))
print(is_positive(n))
print(is_negative(n))
print(is_perfect_square(n))

is_prime = lambda n:'Prime' if n>1 and not any(n% i==0 for i in range(2, int(n**0.5) +1)) else "Not Prime"