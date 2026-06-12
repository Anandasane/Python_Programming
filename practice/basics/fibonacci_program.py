# Problem Statement:
# Write a Python program to print the Fibonacci series and find the nth Fibonacci number.
#
# Intuition:
# Each Fibonacci number is the sum of the previous two Fibonacci numbers.
#
# Input:
series_limit = int(input("Enter number of Fibonacci terms: "))
position = int(input("Enter position to find Fibonacci number: "))

# Logic:
if series_limit <= 0:
    fibonacci_series = []
elif series_limit == 1:
    fibonacci_series = [0]
else:
    fibonacci_series = [0, 1]
    while len(fibonacci_series) < series_limit:
        next_value = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_value)

if position < 0:
    fibonacci_number = "Position must be non-negative."
elif position <= 1:
    fibonacci_number = position
else:
    previous = 0
    current = 1
    for _ in range(2, position + 1):
        previous, current = current, previous + current
    fibonacci_number = current

# Output:
print(f"Fibonacci series: {fibonacci_series}")
print(f"Fibonacci number at position {position}: {fibonacci_number}")
