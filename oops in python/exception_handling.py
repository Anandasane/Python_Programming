
print('Start')

try:
    print(10/0)
except ZeroDivisionError:
    print('Error: Division by zero is not allowed.')

print('End')



try:
    a=int(input("Enter a number"))
except ValueError:
    print('Error: Invalid input. Please enter a valid number.')


try:
    a=10
    b=0
    result=a/b
    print(f'The result of {a} divided by {b} is: {result}')  
except ZeroDivisionError:
    print('this is a zero Division error.')

try:
    # This triggers a TypeError: unsupported operand type(s) for +: 'int' and 'str'
    result = 5 + "10"
except TypeError:
    print('This is a Type Error.')

try:
    # This triggers a NameError: name 'a' is not defined
    print(undefined_variable)
except NameError:
    print('This is a Name error.')

try:
    # This triggers an AttributeError: 'int' object has no attribute 'some_method'
    (123).some_method()
except AttributeError:
    print('This is an Attribute Error.')

try:
    # This triggers a KeyError: 'missing_key'
    my_dict = {"a": 1}
    my_dict["missing_key"]
except KeyError:
    print('This is a key Error.')

try:
    # This triggers an IndexError: list index out of range
    my_list = [1, 2, 3]
    my_list[5]
except IndexError:
    print('This is an Index Error.')

try:
    exec("if True print('x')")
except SyntaxError:
    print('This is a Syntax Error.')

# 6. StopIteration - iterator exhausted
try:
    it = iter([1])
    next(it)
    next(it)
except StopIteration:
    print('This is a Stop Iteration Error.')

# 7. OverflowError - number too large
try:
    import math
    math.exp(1000)
except OverflowError:
    print('This is an Overflow Error.')

# 8. RecursionError - exceeding recursion limit
try:
    def recurse():
        recurse()
    recurse()
except RecursionError:
    print('This is a Recursion Error.')

# 9. MemoryError - (hard to trigger naturally; simulated here)
try:
    raise MemoryError("simulated")
except MemoryError:
    print('This is a Memory Error.')

# 10. PermissionError - no permission to access
try:
    open("/etc/shadow", "w")
except PermissionError:
    print('This is a Permission Error.')

# 11. OSError / IOError - general I/O failure
try:
    open("invalid:filename?.txt")
except OSError:
    print('This is an OS Error.')

# 12. KeyboardInterrupt - user interrupt (simulated with raise)
try:
    raise KeyboardInterrupt
except KeyboardInterrupt:
    print('This is a Keyboard Interrupt.')

# 13. EOFError - no more input
try:
    raise EOFError
except EOFError:
    print('This is an EOF Error.')

# 14. ArithmeticError - base class for numeric errors
try:
    1 / 0
except ArithmeticError:
    print('This is an Arithmetic Error.')

# 15. UnicodeDecodeError - decoding failure
try:
    b'\xff\xfe'.decode('utf-8')
except UnicodeDecodeError:
    print('This is a Unicode Decode Error.')

# 16. TypeError from wrong argument count
try:
    len("a", "b")
except TypeError:
    print('This is a Type Error (wrong argument count).')

# 17. IndexError on string
try:
    "hello"[100]
except IndexError:
    print('This is an Index Error (on a string).')

# 18. KeyError on set-like access via dict
try:
    {}["any_key"]
except KeyError:
    print('This is a Key Error (empty dict).')

# 19. AttributeError on None
try:
    None.upper()
except AttributeError:
    print('This is an Attribute Error (on None).')

# 20. UnboundLocalError - local variable referenced before assignment
try:
    x = 1
    def f():
        print(x)
        x = 2
    f()
except UnboundLocalError:
    print('This is an Unbound Local Error.')


print('=======================================================Multiple Exception===================================================')

