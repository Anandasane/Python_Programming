# Problem Statement:
# Write a Python program to create, read, append, and delete a sample text file.
#
# Intuition:
# File handling uses open/read/write operations to store and retrieve text data.
#
# Input:
line_count = int(input("Enter number of lines to write: "))
lines = [input(f"Enter line {index + 1}: ") for index in range(line_count)]
append_line = input("Enter a line to append: ")

# Logic:
from pathlib import Path

file_path = Path("practice/basics/sample.txt")
file_path.write_text("\n".join(lines), encoding="utf-8")
with file_path.open("a", encoding="utf-8") as file:
    file.write(f"\n{append_line}")
file_lines = file_path.read_text(encoding="utf-8").splitlines()
file_path.unlink()

# Output:
print("File was created, appended, read, and deleted successfully.")
print(f"Lines read before deletion: {file_lines}")
