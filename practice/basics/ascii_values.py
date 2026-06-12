# Problem Statement:
# Write a Python program to find ASCII values of characters and convert ASCII values back to characters.
#
# Intuition:
# The ord() function returns the ASCII value of a character, and chr() returns the character for an ASCII value.
#
# Input:
text = input("Enter text: ")
ascii_input = input("Enter ASCII values separated by spaces: ")

# Logic:
ascii_values = {character: ord(character) for character in text}
characters = "".join(chr(int(value)) for value in ascii_input.split())

# Output:
print(f"Text: {text}")
print(f"ASCII values: {ascii_values}")
print(f"Characters from ASCII values: {characters}")
