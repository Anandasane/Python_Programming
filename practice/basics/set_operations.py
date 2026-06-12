# Problem Statement:
# Write a Python program to perform union, intersection, difference, and symmetric difference on two sets.
#
# Intuition:
# Sets store unique values and support mathematical set operations.
#
# Input:
first_input = input("Enter first set values separated by spaces: ")
second_input = input("Enter second set values separated by spaces: ")

# Logic:
first_set = {int(value) for value in first_input.split()}
second_set = {int(value) for value in second_input.split()}
union_set = first_set | second_set
intersection_set = first_set & second_set
difference_set = first_set - second_set
symmetric_difference = first_set ^ second_set

# Output:
print(f"First set: {first_set}")
print(f"Second set: {second_set}")
print(f"Union: {union_set}")
print(f"Intersection: {intersection_set}")
print(f"Difference: {difference_set}")
print(f"Symmetric difference: {symmetric_difference}")
