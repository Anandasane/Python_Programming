# Problem Statement:
# Write a Python program to check whether a string is a palindrome and reverse the words in a sentence.
#
# Intuition:
# A palindrome remains the same after removing spaces/case and reversing. Words can be reversed by splitting and joining in reverse order.
#
# Input:
text = input("Enter text to check palindrome: ")
sentence = input("Enter a sentence to reverse words: ")

# Logic:
cleaned_text = "".join(character.lower() for character in text if character.isalnum())
is_palindrome = cleaned_text == cleaned_text[::-1]
reversed_words = " ".join(sentence.split()[::-1])

# Output:
print(f"Is palindrome? {is_palindrome}")
print(f"Reversed words: {reversed_words}")
