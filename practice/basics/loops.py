# Problem Statement:
# Write a Python program to calculate the sum of even numbers, print a multiplication table, and count vowels.
#
# Intuition:
# Loops help repeat work for a range of values, and conditions filter values such as even numbers or vowels.
#
# Input:
limit = int(input("Enter the limit: "))
table_number = int(input("Enter the number for multiplication table: "))
text = input("Enter text to count vowels: ")

# Logic:
# Add numbers from 1 to limit only when they are divisible by 2.
even_sum = 0
for number in range(1, limit + 1):
    if number % 2 == 0:
        even_sum += number

# Generate multiplication table values.
table = [table_number * multiplier for multiplier in range(1, 11)]

# Count characters that are vowels.
vowels = "aeiouAEIOU"
vowel_count = 0
for character in text:
    if character in vowels:
        vowel_count += 1

# Output:
print(f"Sum of even numbers up to {limit}: {even_sum}")
print(f"Multiplication table of {table_number}: {table}")
print(f"Vowel count in '{text}': {vowel_count}")
