for i in range(1,9):
    for j in range(1,9):
        
        if(j>=9-i):
            print("*",end=" ")
        else:
            print(" ",end=" ")   
        
    for k in range(1,i):
        print("*",end=" ")

    print()