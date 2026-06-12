# Problem Statement:
# Write a Python program to find two numbers in a list whose sum equals a target value.
#
# Intuition:
# Store each number's index while checking whether the needed complement has already been seen.
#
# Input:
numbers_input = input("Enter numbers separated by spaces: ")
target = int(input("Enter target sum: "))

# Logic:
numbers = [int(value) for value in numbers_input.split()]
seen = {}
result = None
for index, number in enumerate(numbers):
    needed = target - number
    if needed in seen:
        result = (seen[needed], index)
        break
    seen[number] = index

# Output:
if result is None:
    print("No two numbers found with the target sum.")
else:
    print(f"Indices: {result}")
    print(f"Values: {numbers[result[0]]}, {numbers[result[1]]}")
