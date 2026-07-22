
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

