# Problem Statement:
# Write a Python program to check whether two strings are anagrams and group anagrams from a list of words.
#
# Intuition:
# Anagrams contain the same characters, so sorting the characters creates the same key for anagram words.
#
# Input:
first_word = input("Enter first word: ")
second_word = input("Enter second word: ")
words_input = input("Enter words separated by spaces: ")

# Logic:
def normalize(word):
    return "".join(sorted(word.lower()))


is_anagram = normalize(first_word) == normalize(second_word)
groups = {}
for word in words_input.split():
    key = normalize(word)
    groups.setdefault(key, []).append(word)

# Output:
print(f"Are '{first_word}' and '{second_word}' anagrams? {is_anagram}")
print(f"Anagram groups: {groups}")
