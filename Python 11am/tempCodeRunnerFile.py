s=0
while(s<25):
    s+=1
    if(s%5==0):
        print()
    if(s==1 or s==3 or s==5):
        print("0" * 5)
    else:
        print("x"* 5)