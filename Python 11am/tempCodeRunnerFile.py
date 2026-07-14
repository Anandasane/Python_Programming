sum=0
for i in range(1,101):
    
    if(i==80):
        break
    elif(i%8==0):
        continue
    elif(i%4==0):
        sum = sum +i

print("the sum of the numbers is ",sum)
