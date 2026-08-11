b=[10,34,25,34,20,10,20]

for i in range(0,len(b)):
    for j in range(i+1,len(b)):
        if(b[i] == b[j]):
            print(f'{b[i]}: is a duplicate value')
    i+=1

