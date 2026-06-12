# Problem Statement:
# Write a Python program to maintain a simple to-do list.
#
# Intuition:
# A list of dictionaries can store each task title and completion status.
#
# Input:
tasks_input = input("Enter tasks separated by commas: ")

# Logic:
class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, title):
        self.tasks.append({"title": title, "done": False})

    def complete(self, index):
        self.tasks[index]["done"] = True

    def remove(self, index):
        del self.tasks[index]

    def list_tasks(self):
        return self.tasks


todo_list = TodoList()
for task in tasks_input.split(","):
    todo_list.add(task.strip())

if len(todo_list.list_tasks()) > 0:
    todo_list.complete(0)

formatted_tasks = []
for index, task in enumerate(todo_list.list_tasks(), start=1):
    status = "x" if task["done"] else " "
    formatted_tasks.append(f"{index}. [{status}] {task['title']}")

# Output:
print("To-do list:")
print("\n".join(formatted_tasks) if formatted_tasks else "No tasks added.")
