print('============================================')

try:
    i=int(input('enter your name : '))
except Exception as e:
    print('Error: ', e)
else:
    print('you can login')

finally: 
    print('thank you for your time ')