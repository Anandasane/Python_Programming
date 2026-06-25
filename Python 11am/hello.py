print("hello world")

list = [12,24,53,6,466,7,8,9,10]
# for i in list:
#     print(i)

# for i in range(len(list)):
#     print(list[i])

#     print(list[i], end=" ")

# calculator 

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

switch = input("Enter the operation (+, -, *,/): ")
if switch == "+":
    print(a+b)
elif switch == "-":
    print(a-b)
elif switch == "*":
    print(a*b)
elif switch == "/":
    print(a/b)
else:
    print("Invalid operation")