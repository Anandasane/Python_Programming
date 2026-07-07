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


# 2
