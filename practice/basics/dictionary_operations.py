# Problem Statement:
# Write a Python program to store key-value pairs in a dictionary and merge two dictionaries.
#
# Intuition:
# Dictionaries store values by keys and can be merged by updating one dictionary with another.
#
# Input:
first_pairs = input("Enter first dictionary pairs as key:value separated by commas: ")
second_pairs = input("Enter second dictionary pairs as key:value separated by commas: ")

# Logic:
def parse_pairs(text):
    result = {}
    for pair in text.split(","):
        key, value = pair.split(":")
        result[key.strip()] = int(value.strip())
    return result


first_dictionary = parse_pairs(first_pairs)
second_dictionary = parse_pairs(second_pairs)
merged_dictionary = first_dictionary.copy()
merged_dictionary.update(second_dictionary)

# Output:
print(f"First dictionary: {first_dictionary}")
print(f"Second dictionary: {second_dictionary}")
print(f"Merged dictionary: {merged_dictionary}")
