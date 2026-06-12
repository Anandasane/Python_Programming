# Problem Statement:
# Write a Python program to perform operations on lists, tuples, and sets.
#
# Intuition:
# Lists store ordered values, tuples store fixed ordered values, and sets store unique values.
#
# Input:
list_input = input("Enter list values separated by spaces: ")
first_tuple_value = input("Enter first tuple value: ")
second_tuple_value = input("Enter second tuple value: ")
first_set_input = input("Enter first set values separated by spaces: ")
second_set_input = input("Enter second set values separated by spaces: ")

# Logic:
numbers = [int(value) for value in list_input.split()]
sorted_numbers = sorted(numbers)
unique_numbers = set(numbers)
sample_tuple = (first_tuple_value, second_tuple_value)
first_set = set(first_set_input.split())
second_set = set(second_set_input.split())
union_set = first_set | second_set
intersection_set = first_set & second_set
difference_set = first_set - second_set

# Output:
print(f"Original list: {numbers}")
print(f"Sorted list: {sorted_numbers}")
print(f"Unique numbers: {unique_numbers}")
print(f"Tuple: {sample_tuple}")
print(f"Set union: {union_set}")
print(f"Set intersection: {intersection_set}")
print(f"Set difference: {difference_set}")
