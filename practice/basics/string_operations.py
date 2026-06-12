# Problem Statement:
# Write a Python program to perform common string operations.
#
# Intuition:
# Strings can be split into words, counted by characters, filtered for vowels, and reversed word-by-word.
#
# Input:
text = input("Enter a text: ")

# Logic:
words = text.split()
word_count = len(words)
character_count = len(text)
vowels = "aeiouAEIOU"
vowel_count = sum(1 for character in text if character in vowels)
reversed_words = " ".join(words[::-1])

# Output:
print(f"Text: {text}")
print(f"Word count: {word_count}")
print(f"Character count: {character_count}")
print(f"Vowel count: {vowel_count}")
print(f"Reversed words: {reversed_words}")
