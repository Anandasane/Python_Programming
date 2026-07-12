# for loop in python
for i in range(1,101):
    print(i)

# printing only even number from 1 to 100
for i in range(1,101):
    if(i%2==0):
        print(i)

for i in range(0,101,2):
    print(i)

for i in range(1,101):
    if(i%2==0 and i%5==0 and i%10==0):
        print(i)

# counting the even number
n=int(input("Enter a number: "))
c=0
for i in range(1,n+1):
    if(i%2==0):
        print(i)
        c+=1

print("count is: ",c)

# printing the sum of numbers 
n= int(input("Enter a number: "))
sum =0
for i in range(1,n+1):
    sum = sum+i

print("the sum of the numbers is: ",sum)

# counting the vowel and consonent in the string
s=input("Enter a string: ")
v=0
c=0
for i in range(0,len(s)):
    if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A'  or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U'):
        v+=1
    else:
        c+=1
print("the total number of vowel are: ",v)
print("the total number of consonent are: ",c)

# printing a mutliplication table for input number

n=int(input("Enter the number: "))

for i in range(1,11):
    print(f"2 x {i}= {2*i}")

# printing the factorial for input number

n=int(input("Enter a number: "))
f=1
for i in range(1,n+1):
    f=f*i

print("the factorial of the number is:",f)

# printing the count of number which cannot be divisible by 2,5,10 using continue keyword

n=int(input("Enter the number: "))
c=0
for i in range(1,n+1):
    if(i%2==0 and i%5==0 and i%10==0):
        continue
    else:
        print(i)
        c+=1

print("the count of the number is: ",c)

# code to check wheather the password is correct or not

correct_pass ="123"

for i in range(1,100):
    userpass=input("Enter you password: ")
    if(userpass==correct_pass):
        print("you have succesfully logged in ")
        break
    else:
        print("try Again")
        
    