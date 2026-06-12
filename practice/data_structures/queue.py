# Problem Statement:
# Write a Python program to implement a queue using deque.
#
# Intuition:
# A queue follows First In First Out, so items leave from the front.
#
# Input:
items_input = input("Enter queue items separated by spaces: ")

# Logic:
from collections import deque

queue = deque()
for item in items_input.split():
    queue.append(item)

served_items = []
while len(queue) > 0:
    served_items.append(queue.popleft())

# Output:
print(f"Served queue items: {served_items}")
