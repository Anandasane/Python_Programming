is_prime = lambda n:"Prime" if n > 1 and not any(n % i == 0 for i in range(2, int(n**0.5) + 1)) else "Not Prime"
a = int(input('Enter a number: '))
print(is_prime(a))
