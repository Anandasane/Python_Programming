
print('Start')

try:
    print(10/0)
except ZeroDivisionError:
    print('Error: Division by zero is not allowed.')

print('End')


try: 
    a=int(input('Enter a number: '))
except ValueError:
    print('Error: Invalid input. Please enter a valid number.')


try:
    b=int(input('Enter another number: '))
except ValueError:
    print('Error: Invalid input. Please enter a valid number.')


try:
    result=a/b
    print('Result:', result)
except ZeroDivisionError:
    print('Error: Division by zero is not allowed.')

except typeError:
    print('Error: Invalid input. Please enter a valid number.')

except boundaryError:
    print('Error: Invalid input. Please enter a valid number.')

except indexError:
    print('Error: Invalid input. Please enter a valid number.')

except AttributeError:
    print('Error: Invalid input. Please enter a valid number.')

except valueError:
    print('Error: Invalid input. Please enter a valid number.')

except error:
    print('Error: Invalid input. Please enter a valid number.')