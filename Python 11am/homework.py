# homework problems 
# Problem 1 Print numbers from 1 to 20. Stop the loop when the number becomes 10.
for i in range(1,21):
    print(i)
    if(i==10):
        break

# Problem 2 Accept a number from the user. Stop printing numbers when the entered number is reached

no=int(input("Enter a number: "))
for i in range(1,no+1):
    print(i)

# Problem 3 Print numbers from 100 to 1. Stop when you reach 50.

for i in range(100,0,-1):
    print(i)
    if(i==50):
        break

# Problem 4 Print even numbers from 1 to 100. Stop when you reach 40.

for i in range(1,101):
    if(i%2==0):
        print(i)
        if(i==40):
            break
    

# Problem 5 Print odd numbers from 1 to 100. Stop when you reach 51.

for i in range(1,101):
    if(i%2==1):
        print(i)
        if(i==51):
            break
    

# Problem 6 Print the multiplication table of a number. Stop after the 5th multiplication.

n=int(input("Enter the number: "))

for i in range(1,11):
    print(f"{n} x {i}= {n*i}")
    if(i==5):
        break


# Problem 7 Print numbers from 1 to 100. Stop when you find the first number divisible by both 7 and 9.

for i in range(1,101):
    if(i%7==0 and i%9==0):
        break
    else:
        print(i)
    
# Problem 8 Print the Fibonacci series. Stop when a term becomes greater than 100.
n=int(input("Enter the number: "))

a,b=0,1
for i in range(1,n+1):
    print(a)
    a, b = b, a + b


# Problem 9 Print factors of a number. Stop after finding the first factor greater than 10.
n=int(input("Enter a number: "))

for i in range(1,n+1):
    if(n%i==0 ):
        print(i)
        if(i>=10):
            break


# Problem 10 Print numbers from 1 to 50. Stop when the square of a number is greater than 500.
for i in range(1 ,51):
    if(i*i<=500):
        print(i)

# Problem 11 Print alphabet letters from A to Z. Stop at M.
for i in range(65,91):
    if(i<=77):
        print(chr(i))

# Problem 12 Print numbers from 1 to 30. Stop when the user-entered number appears.
n=int(input("Enter a number: "))
for i in range(1,31):
    if(i!=n):
        print(i)
    else:
        break

# Problem 13 Print numbers from 1 to 100. Stop when a multiple of 13 is found.
for i in range(1,101):
    if(i%13==0):
        break
    else:
        print(i)
    

# Problem 14 Print numbers from 1 to 100. Stop after printing 20 numbers.
for i in range(1,101):
    if(i==21):
        break
    else:
        print(i)

# Problem 15 Print the multiplication tables from 1 to 10. Stop after table 5.

for i in range(1,11):
    if(i>5):
        break
    else:
        print(f"Table of {i}: ")
        for j in range(1,11):
            print(f"{i} x {j} = {i*j} ")
        print()


# Problem 16 Print numbers from 1 to 20, skipping 10.
for i in range(1,21):
    
    if(i==10):
        continue
    else:
        print(i)
        
        
# Problem 17 Print even numbers from 1 to 50, skipping 20.
for i in range(1,51):
   if(i%2==0): 
        if(i==20):
            continue
        else:
            print(i)
            
# Problem 18 Print odd numbers from 1 to 50, skipping 25.
for i in range(1,51):
   if(i%2!=0): 
        if(i==25):
            continue
        else:
            print(i)
            

# Problem 19 Print numbers from 1 to 100, skipping multiples of 5.
for i in range(1,101):
    
    if(i%5==0):
        continue
    else:
        print(i)
        

# Problem 20 Print numbers from 1 to 100, skipping multiples of 3.
for i in range(1,101):
    
    if(i%3==0):
        continue
    else:
        print(i)
        

# Problem 21 Print numbers from 1 to 50, skipping numbers divisible by both 2 and 3.
for i in range(1,50):
    
    if(i%2==0 or i%3==0):
        continue
    else:
        print(i)
        
# Problem 22 Print the multiplication table of a number, skipping the 5th multiplication.
n=int(input("Enter a number: "))
for i in range(1,11):
    if(i==5):
        continue
    else:
        print(f"{n} x {i} = {n*i}")


# Problem 23 Print numbers from 1 to 100, skipping prime numbers.
#method 1
# for i in range(1, 101):
#     if i == 1:
#         print(i)
#         continue

#     is_prime = True
#     # Check divisors from 2 up to the square root of i
#     for j in range(2, int(i**0.5) + 1):
#         if i % j == 0:
#             is_prime = False
#             break  # Found a factor, so it's not prime

#     # If is_prime is still True, it means no factors were found
#     if not is_prime:
#         print(i)

# method 2

for num in range(1, 101):
    if num < 2:
        print(num)
        continue

    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        continue  # Skip prime numbers

    print(num)



# Problem 24 Print numbers from 1 to 100, skipping perfect squares.
for i in range(1, 101):
    root =int(i**0.5)
    
    if root * root == i:
        continue  
    else:
        print(i)

# Problem 25 Print numbers from 1 to 50, skipping numbers ending with 5.

for i in range(1,51):
    if(i%10==5):
        continue
    else:
        print(i)

# Problem 26 Print alphabet letters from A to Z, skipping vowels.
for i in range(65,91):
    if(i == 65 or i == 69 or i == 73 or i == 79 or i == 85):
        continue
    else:
        print(chr(i))

# Problem 27 Print numbers from 1 to 100, skipping numbers divisible by 7.
for i in range(1,101):
    if(i%7==0):
        continue
    else:
        print(i)

# Problem 28 Print numbers from 1 to 30, skipping all even numbers.
for i in range(1,31):
    if(i%2==0):
        continue
    else:
        print(i)

# Problem 29 Print numbers from 50 to 1, skipping multiples of 4.
for i in range(1,31):
    if(i%4==0):
        continue
    else:
        print(i)
# Problem 30 Print numbers from 1 to 100, skipping numbers between 40 and 60 (inclusive).
for i in range(1,101):
    if(i>=40 and i<=60):
        continue
    else:
        print(i)

