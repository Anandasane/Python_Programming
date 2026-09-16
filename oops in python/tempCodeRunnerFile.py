print('---------------------')

try:
    u=int(input('Enter you name: '))
    raise Exception("Name should be Sting ")
except Exception as e:
    print("Error: ",e)
else:
    print('Thankyou')