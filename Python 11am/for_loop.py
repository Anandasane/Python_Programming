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


n=int(input("Enter a number: "))
c=0
for i in range(1,n+1):
    if(i%2==0):
        print(i)
        c+=1

print("count is: ",c)

n= int(input("Enter a number: "))
sum =0
for i in range(1,n+1):
    sum = sum+i

print(sum)

s=input("Enter a string: ")
v=0
 
for i in range(0,len(s)):
    if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A'  or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U'):
        v+=1

print(v)