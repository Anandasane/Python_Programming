# Problem Statement:
# Write a Python program to search for a target using linear search and binary search.
#
# Intuition:
# Linear search checks each element one by one. Binary search repeatedly divides a sorted list in half.
#
# Input:
numbers_input = input("Enter sorted numbers separated by spaces: ")
target = int(input("Enter target number: "))

# Logic:
numbers = [int(value) for value in numbers_input.split()]


def linear_search(values, search_target):
    for index, value in enumerate(values):
        if value == search_target:
            return index
    return -1


def binary_search(values, search_target):
    left = 0
    right = len(values) - 1
    while left <= right:
        middle = (left + right) // 2
        if values[middle] == search_target:
            return middle
        if values[middle] < search_target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


linear_index = linear_search(numbers, target)
binary_index = binary_search(numbers, target)

# Output:
print(f"Linear search index: {linear_index}")
print(f"Binary search index: {binary_index}")
