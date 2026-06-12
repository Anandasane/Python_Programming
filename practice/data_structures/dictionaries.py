# Problem Statement:
# Write a Python program to find word frequency and group words by their length using dictionaries.
#
# Intuition:
# A dictionary can count repeated words by increasing the count for each key.
#
# Input:
text = input("Enter text: ")
words_input = input("Enter words separated by spaces: ")

# Logic:
words = text.lower().replace(".", "").replace(",", "").split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

grouped_by_length = {}
for word in words_input.split():
    grouped_by_length.setdefault(len(word), []).append(word)

# Output:
print(f"Word frequency: {frequency}")
print(f"Words grouped by length: {grouped_by_length}")
