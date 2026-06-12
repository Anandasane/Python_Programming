# Problem Statement:
# Write a Python program to implement a stack and reverse a string using stack operations.
#
# Intuition:
# A stack follows Last In First Out, so the last pushed character is popped first.
#
# Input:
text = input("Enter text to reverse using stack: ")

# Logic:
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


stack = Stack()
for character in text:
    stack.push(character)

reversed_text = ""
while not stack.is_empty():
    reversed_text += stack.pop()

# Output:
print(f"Original text: {text}")
print(f"Reversed text: {reversed_text}")
