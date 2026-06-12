# Problem Statement:
# Write a Python program to find sum, average, minimum, maximum, and remove duplicates from a list.
#
# Intuition:
# Lists can be processed with built-in functions, and dict.fromkeys preserves first occurrence order while removing duplicates.
#
# Input:
numbers_input = input("Enter numbers separated by spaces: ")

# Logic:
numbers = [int(value) for value in numbers_input.split()]
summary = {
    "sum": sum(numbers),
    "average": sum(numbers) / len(numbers),
    "minimum": min(numbers),
    "maximum": max(numbers),
    "count": len(numbers),
}
without_duplicates = list(dict.fromkeys(numbers))

# Output:
print(f"Numbers: {numbers}")
print(f"List summary: {summary}")
print(f"Without duplicates: {without_duplicates}")
