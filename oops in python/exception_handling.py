
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
    a=
except ValueError:
    print('Error: Invalid input. Please enter a valid number.')


try:
    result=a/b
    print(f'The result of {a} divided by {b} is: {result}')  
except ZeroDivisionError:
    print('this is a zero Division error.')

try:
    a=
except TypeError:
    print('this is a Type Error.')

try:
    a=
except NameError:
    print('This is Name error.')

try:
    a=
except ValueError:
    print('This is a  Value Error.')

try:
    a=
except AttributeError:
    print('This is a Attribute Error.')

try:
    a=
except KeyError:
    print('This is a key Error.')

try:
    a=
except IndexError:
    print('This is an Index Error.')