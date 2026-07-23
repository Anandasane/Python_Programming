
a=1

while(a<10):
   print("hello")

n=int(input("Enter a number: "))
a=1
while(a<10):
    print(f"{n} X {a} = {n*a}")
    a+=1


s=11
while(True):
   n = int(input("Enter your password: "))
   if(n==s):
      print("sucessfully loged in !") 
      break
   else:
      print("Try Again")  



user="abc"
p=123

while(True):
    username=input("Enter your username: ")
    if(user==username):
      ps=int(input("Enter your password: "))
      if(p==ps):
        print("Successfully loged in ")
        break
      else:
        print("invalid password , Try again")  

# practise questions
# 1. Print numbers from 1 to 20. Stop the loop when the number becomes 10.

num =1
while(num<=20):
   print(num)
   num+=1
   if(num==10):
      break

# 2. Accept a number from the user. Stop printing numbers when the entered number is reached.

n=int(input("Enter a number: "))
i=0
while(i<n):
   print(i)
   i+=1

# 3. Print numbers from 100 to 1. Stop when you reach 50.

i=100
while(i<=100):
   print(i)
   i-=1
   if(i==50):
      break

# 4. Print even numbers from 1 to 100. Stop when you reach 40.

i=2
while(i<=100):
   if(i==40):
         break
   if(i%2==0):
      print(f"{i} is even ")
   else:
      print(f"{i} is odd ")
   i+=1
   

#  5. Print odd numbers from 1 to 100. Stop when you reach 51.

num = 1
while num <= 100:
    if num == 51:
        break
    if num % 2 != 0:
        print(num)
    num += 1

# 6. Print the multiplication table of a number. Stop after the 5th multiplication.

n = int(input("Enter a number: "))
i = 1
while i <= 10:
    if i == 6:
        break
    print(f"{n} x {i} = {n * i}")
    i += 1

# 7. Print numbers from 1 to 100. Stop when you find the first number divisible by both 7 and 9.

i=1 
while(i<=100):
   print(i)
   i+=1
   if(i%7==0 and i%9==0):
      break

# 8. Print the Fibonacci series. Stop when a term becomes greater than 100.

a, b = 0, 1
while a <= 100:
    print(a, end=" ")
    temp = a + b  
    a = b         
    b = temp      

a, b = 0, 1
while a <= 100:
    print(a, end=" ")
    a, b = b, a + b

# 9. Print factors of a number. Stop after finding the first factor greater than 10.

n=int(input("Enter a number: "))
i=1
while(i<n):
   if(i>=10):
      break
   if(n%i==0):
      print(f"{i} is a factor of : {n} ")
   i+=1

# 10. Print numbers from 1 to 50. Stop when the square of a number is greater than 500.

i=1
while(i<=50):
   if(i*i>=500):
      break
   else:
      print(i)
   i+=1

# 11. Print alphabet letters from A to Z. Stop at M.

letter = ord('A')
while letter <= ord('Z'):
    if chr(letter) == 'M':
        break
    print(chr(letter), end=" ")
    letter += 1

# 12. Print numbers from 1 to 30. Stop when the user-entered number appears.

limit = int(input("Enter a number: "))
num = 1
while num <= 30:
    if num == limit:
        break
    print(num)
    num += 1

# 13. Print numbers from 1 to 100. Stop when a multiple of 13 is found.

num = 1
while num <= 100:
    if num % 13 == 0:
        print(f"First multiple of 13: {num}")
        break
    num += 1

# 14. Print numbers from 1 to 100. Stop after printing 20 numbers.

num = 1
count = 1
while num <= 100:
    if count > 20:
        break
    print(num)
    num += 1
    count += 1

# 15. Print the multiplication tables from 1 to 10. Stop after table 5.

table = 1
while table <= 10:
    if table == 6:
        break
    print(f"\nTable of {table}")
    i = 1
    while i <= 10:
        print(f"{table} x {i} = {table * i}")
        i += 1
    table += 1

# 16. Print numbers from 1 to 20, skipping 10.

num = 1
while num <= 20:
    if num == 10:
        num += 1
        continue
    print(num)
    num += 1

# 17. Print even numbers from 1 to 50, skipping 20.

num = 1
while num <= 50:
    if num == 20:
        num += 1
        continue
    if num % 2 == 0:
        print(num)
    num += 1

# 18. Print odd numbers from 1 to 50, skipping 25.

num = 1
while num <= 50:
    if num == 25:
        num += 1
        continue
    if num % 2 != 0:
        print(num)
    num += 1

# 19. Print numbers from 1 to 100, skipping multiples of 5.

num = 1
while num <= 100:
    if num % 5 == 0:
        num += 1
        continue
    print(num)
    num += 1

# 20. Print numbers from 1 to 100, skipping multiples of 3.

num = 1
while num <= 100:
    if num % 3 == 0:
        num += 1
        continue
    print(num)
    num += 1

# 21. Print numbers from 1 to 50, skipping numbers divisible by both 2 and 3.

num = 1
while num <= 50:
    if num % 2 == 0 and num % 3 == 0:
        num += 1
        continue
    print(num)
    num += 1

# 22. Print the multiplication table of a number, skipping the 5th multiplication.

n = int(input("Enter a number: "))
i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(f"{n} x {i} = {n * i}")
    i += 1

# 23. Print numbers from 1 to 100, skipping prime numbers.

num = 2
while num <= 100:
    is_prime = True
    i = 2
    while i <= num // 2:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime and num > 1:
        num += 1
        continue
    print(num)
    num += 1

# 24. Print numbers from 1 to 100, skipping perfect squares.

num = 1
while num <= 100:
    i = 1
    is_square = False
    while i * i <= num:
        if i * i == num:
            is_square = True
            break
        i += 1
    if is_square:
        num += 1
        continue
    print(num)
    num += 1

# 25. Print numbers from 1 to 50, skipping numbers ending with 5.

num = 1
while num <= 50:
    if num % 10 == 5:
        num += 1
        continue
    print(num)
    num += 1

#26. Print alphabet letters from A to Z, skipping vowels.

letter = ord('A')
vowels = ['A', 'E', 'I', 'O', 'U']
while letter <= ord('Z'):
    if chr(letter) in vowels:
        letter += 1
        continue
    print(chr(letter), end=" ")
    letter += 1

#27. Print numbers from 1 to 100, skipping numbers divisible by 7.

num = 1
while num <= 100:
    if num % 7 == 0:
        num += 1
        continue
    print(num)
    num += 1

# num = 1
while num <= 30:
    if num % 2 == 0:
        num += 1
        continue
    print(num)
    num += 1

# 29. Print numbers from 50 to 1, skipping multiples of 4.

num = 50
while num >= 1:
    if num % 4 == 0:
        num -= 1
        continue
    print(num)
    num -= 1

# 30. Print numbers from 1 to 100, skipping numbers between 40 and 60 (inclusive).

num = 1
while num <= 100:
    if 40 <= num <= 60:
        num += 1
        continue
    print(num)
    num += 1


s=100
while(s>0):
    if(s%5==0):
        s-=1
        continue
    print(s)
    s-=1