# Pattern printing in python

# 1 star pattern

for i in range(1,4):
    for j in range(1,4):
        print("*",end=" ")

    print()

# number instead of star

for i in range(1,5):
    for j in range(1,5):
        print(j,end=" ")
    
    print()


c=0
for i in range(1,4):
    for j in range(1,6):
        c=c+1
        print(c,end=" ")

    print()

# for i in range(1,40):
    
#     if(i%5==0):
#         continue
#     elif(i>=1 and i<=10):
#         print(i,end=" ",)
#         break
#     elif(i>=11 and i<=20):
        
#         print(i,end=" ",)
        
#     elif(i>=21 and i<=30):
        
#         print(i,end=" ",)
#     else:
        
#         print(i,end=" ",)


# wrong
for i in range(1,70):
    if(i==10 or i==20 or i==30):
        print()

    if(i%5==0):
        continue
    print(i,end=' ')

# correct
for i in range(1,40):
    if(i%10==0):
        print()

    if(i%5==0 or i%6==0):
        continue
    print(i,end=' ')

for i in range(1,4):
    for j in range(1,7):
        if(j%2==0):
            print('X',end=" ")
        else:
            print('0',end=" ")
    print()

for i in range(1,4):
    for j in range(1,7):
        if((i+j)%2==0):
            print('X',end=" ")
        else:
            print('0',end=" ")
    print()

