# Problem Statement:
# Write a Python program to print the FizzBuzz sequence up to a given limit.
#
# Intuition:
# Numbers divisible by both 3 and 5 print FizzBuzz, by 3 print Fizz, and by 5 print Buzz.
#
# Input:
limit = int(input("Enter limit: "))

# Logic:
result = []
for number in range(1, limit + 1):
    if number % 15 == 0:
        result.append("FizzBuzz")
    elif number % 3 == 0:
        result.append("Fizz")
    elif number % 5 == 0:
        result.append("Buzz")
    else:
        result.append(str(number))

# Output:
print("\n".join(result))
