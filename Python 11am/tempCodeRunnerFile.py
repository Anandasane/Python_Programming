for i in range(9,0,-1):
    for j in range(1,9):
        
        if(j>=i):
            print("*",end=" ")
        else:
            print(" ",end=" ")   
        
        for k in range(2*i-1):
            print("*")

    print()