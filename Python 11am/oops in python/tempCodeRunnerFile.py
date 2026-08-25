a=[-24,42,5,3,2,-5,5,-24,-54,-23]
def positive_number(a):
    b=[]
    for i in range(len(a)):
        
        if(a[i]>0):
           yield a[i] 
           b.append(a[i])
           i+=1
        #     print("Positive elements in list are: ",a[i])
        #     i+=1
        # else: 
        #     print('negative elements in list are: ',a[i])
        #     i+=1
        # return b
    return b
c=positive_number(a)
print(c)