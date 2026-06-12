# Problem Statement:
# Write a Python program to sort a list using bubble sort, insertion sort, and merge sort.
#
# Intuition:
# Sorting algorithms rearrange elements into order. Bubble sort swaps adjacent elements, insertion sort builds a sorted part, and merge sort divides and merges.
#
# Input:
numbers_input = input("Enter numbers separated by spaces: ")

# Logic:
numbers = [int(value) for value in numbers_input.split()]


def bubble_sort(values):
    result = values.copy()
    for index in range(len(result)):
        swapped = False
        for inner_index in range(0, len(result) - index - 1):
            if result[inner_index] > result[inner_index + 1]:
                result[inner_index], result[inner_index + 1] = result[inner_index + 1], result[inner_index]
                swapped = True
        if not swapped:
            break
    return result


def insertion_sort(values):
    result = values.copy()
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result


def merge_sort(values):
    if len(values) <= 1:
        return values
    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])
    return merge(left, right)


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


bubble_result = bubble_sort(numbers)
insertion_result = insertion_sort(numbers)
merge_result = merge_sort(numbers)

# Output:
print(f"Original list: {numbers}")
print(f"Bubble sort: {bubble_result}")
print(f"Insertion sort: {insertion_result}")
print(f"Merge sort: {merge_result}")
