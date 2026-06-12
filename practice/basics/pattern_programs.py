# Problem Statement:
# Write a Python program to print common number and star patterns.
#
# Intuition:
# Nested loops can print repeated characters row by row.
#
# Input:
rows = int(input("Enter number of rows: "))

# Logic:
right_angle_triangle = ["*" * row for row in range(1, rows + 1)]
inverted_triangle = ["*" * row for row in range(rows, 0, -1)]
number_pyramid = [str(row) * row for row in range(1, rows + 1)]

# Output:
print("Right angle triangle:")
print("\n".join(right_angle_triangle))
print("\nInverted triangle:")
print("\n".join(inverted_triangle))
print("\nNumber pyramid:")
print("\n".join(number_pyramid))
