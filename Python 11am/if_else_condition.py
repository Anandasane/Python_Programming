# loops in python
# if else condition

user = int(input("Enter your marks:"))

if(user >= 35):
    print("You are pass")
else:
    print("You are fail")

user = int(input("Enter your temperature: "))    

if(user > 100):
    print("You have fever")
else:
    print("you dont have fever")


# nested if else condition

user = int(input("Enter your marks: "))

if(user >= 35):
    print("You are pass")
    if(user >= 90):
        print("You are excellent")
    else:
        print("You are good")
else:
    print("You are fail")

# multilevel if else condition

user = int(input("Enter your marks: "))

if(user >= 35):
    print("You are pass")
    if(user >= 90):
        print("You are excellent")
    else:
        print("You are good")
else:
    print("You are fail")

# multiple if else condition

user = float(input("Enter your BMI: "))

if(user == 18.5):
    print(" you are skinny")
    if(user<24.9):
        print("You are fit ")
else:
    print("you are overweight")


# elif loop
marks = int(input("Enter your marks: "))

if(marks >90):
    print("A+")
elif(marks >80):
    print("B+")
elif(marks >70):
    print("C+")
elif(marks >60):   
    print("D+")
else:
    print("Fail")

# for given range

temp = int(input("Enter your temperature: "))

if(temp>=20 and temp<=50):
    print("You are healthy")
elif(temp>=50 and  temp<=100):
    print("You have fever")
elif(temp>=100 and temp<=150):
    print("You have high fever")
else:
    print("You are in critical condition")


m = int(input("Enter your marks: "))

if(m<=0 or m>100):
    print("Invalid marks")
elif(m>=90 and m<=100):
    print("A+")
elif(m>=80 and m<=90):
    print("B+")
elif(m>=70 and m<=80):
    print("C+")
elif(m>=60 and m<=70):
    print("D+")
elif(m>=35 and m<=60):
    print("E+")
else:
    print("you have failed")


budget = int(input("Enter your budget: "))

if(budget<= 10000):
    print("you can't buy phone")
elif(budget>=10000 and budget<=20000):
    print("you can buy \n Realme P4x,\n Samsung A16 5G,\n Honor 200")
elif(budget>=20000 and budget<=30000):
    print("you can buy \n Samsung A34,\n Realme 12x,\n Poco X5 Pro")
elif(budget>=30000 and budget<=40000):
    print("you can buy \n Samsung A54,\n Oneplus Nord 3,\n Realme 12 Pro+")
elif(budget>=50000 and budget<=90000):
    print("you can buy \nSamsung S23,\n Oneplus 11,\n Realme GT 3")
elif(budget>=100000 and budget<=200000):
    print("you can buy \n Samsung S23 Ultra,\n Oneplus 11R,\n Realme GT 3 Master Edition")
else:
    print("you can buy any of the phone")


# Problem 1 check if the number is positive negative or zero

number = int(input("Enter the number: "))

if(number==0):
    print("The number is zero")
elif(number<0):
    print("The number is negative number")
else:
    print("The number is positive number") 

# Problem 2 Finding the largest of 3 number

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))

if(a>b and a>c):
    print(a," is the greatest number")
elif(b>a and b>c):
    print(b," is the greatest number ")
else:
    print(c," is the greatest number ")

# Problem 3 finding the smallest from the 4 numbers

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
d=int(input("Enter the fourt number: "))

if(a<b and a<c and a<d):
    print(a," is the smallest number")
elif(b<a and b<c and b<d):
    print(b," is the smallest number")
elif(c<a and c<b and c<d):
    print(c," is the smallest number")
else:
    print(d," is the smallest number")

# Problem 4 check wheather a year is leap year

year=int(input("Enter the year you want to check: "))

if(year%4==0 or year%400==0):
    print("it is a leap year")
else:
    print("it is a normal year")

# Problem 5 Check whether a character is a vowel or consonant

a=(input("Enter a character: "))

if(a=="a" or a=="e" or a=="i" or a=="o" or a=="u" or a=="A" or a=="E" or a=="I" or a=="O" or a=="U"):
    print("the character is vowel")
else:
    print("the charcter is consonant")

# Problem 6 Check whether a character is uppercase, lowercase, digit, or special character

a=input("Enter a character: ")
 
if a.isdigit():
    print("Character is a numeric digit (integer type).")  
elif a.islower():
    print("Character is a lowercase letter.")  
elif a.isupper():
    print("Character is an uppercase letter.")
else:
    print("Character is a special symbol or punctuation.")

# Problem 7 Find whether a number is even or odd

no = int(input("Enter a number: "))

if(no%2==0):
    print("the number is even")
else:
    print("the number is odd")

# Problem 8 Check whether a person is eligible to vote (age ≥ 18).

age =int(input("Enter your age: "))

if(age>=18):
    print("you are eligible to vote ")
else:
    print("you are not eligible to vote")

# Problem 9 Calculate electricity bill based on slabs.

bill=int(input("Enter your bill: "))

if(bill<=0):
    print("invlaid amount ")
elif(bill>50 and bill<100):
    print("you have a less electricity consumption")
elif(bill>100 and bill<500):
    print("you have medium electricity consumption")
else:
    print("you have high electricity consumption")

# Problem 10 Calculate income tax based on salary slabs.

sal=int(input("Enter your salary: "))

if(sal<=0):
    print("Enter a valid amount")
elif(sal>0 and sal<=800000):
    print("You need to pay 0'%' income tax")
elif(sal>=800000 and sal<=1500000):
    print("You need to pay 5'%' income tax")
else:
    print("You need to pay 15'%' income tax")

# Problem 11 Find grade from marks (A, B, C, D, F).

marks=int(input("Enter your marks: "))

if(marks<=0):
    print("Enter valid marks")
elif(marks>0 and marks<35):
    print("you have failed better luck next time")
elif(marks>=35 and marks<=60):
    print("F grade")
elif(marks>60 and marks<=70):
    print("D grade")
elif(marks>70 and marks<=80):
    print("C grade")
elif(marks>80 and marks<=90):
    print("B grade")
else:
    print("A grade")

# Problem 12 Check whether a triangle is valid using three angles.

a=float(input("Enter the 1st angle of the triangle: "))
b=float(input("Enter the 2nd angle of the triangle: "))
c=float(input("Enter the 3rd angle of the triangle: "))

if(a+b+c==180 and a > 0 and b > 0 and c > 0):
    print("it ia a valid Triangle")
else:
    print("it is not a valid Triangle")