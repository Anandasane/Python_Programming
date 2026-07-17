
#Question 1: Number Analyzer

# Write a Python program to print numbers from 1 to 100.

# Conditions:

# Print "Even" if the number is even.
# Print "Odd" if the number is odd.
# Skip all numbers divisible by 7 using continue.
# Stop the loop when the number reaches 85 using break

for i in range(1,101):
    if(i==85):
        break
    elif(i%7==0):
        continue
    elif(i%2==0):
        print(i,"Even")
    else:
        print(i,"Odd")




# Question 2: Sum of Selected Numbers

# Write a Python program to find the sum of numbers from 1 to 100.

# Conditions:

# Add only numbers divisible by 4.
# Skip numbers divisible by 8 using continue.
# Stop the loop when the number becomes 80 using break.
# Print the final sum.

sum=0
for i in range(1,101):
    
    if(i==80):
        break
    elif(i%8==0):
        continue
    elif(i%4==0):
        sum = sum +i

print("the sum of the numbers is ",sum)

# Question 3: Count Positive Conditions

# Write a Python program to print numbers from 1 to 100.

# Conditions:

# Count how many numbers are divisible by 3.
# Skip numbers divisible by 9 using continue.
# Stop the loop when the number reaches 75 using break.
# Print the final count.


c=0
for i in range(1,101):
    if(i==75):
        break
    elif(i%9==0):
        continue
    elif(i%3==0):
        print(i)
        c+=1


print("the count of the number divisible by 3 is ",c)

# 4 Write a program for print 1 to n number table using nested for loop

n= int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,11):
        print(f"{i} X {j}={i*j}")
    print()


# 5 Write a program find factorial 1 to n number using nested for

n=int(input("Enter a number: "))

for i in range(1,n+1):
    f=1
    for j in range(1,i+1):
      f=f*j
    print(f"the factorial of the number {i} is:",f)
