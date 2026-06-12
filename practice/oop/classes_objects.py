# Problem Statement:
# Write a Python program to create a class, object, and use object methods.
#
# Intuition:
# A class defines a blueprint, and an object stores real values created from that blueprint.
#
# Input:
name = input("Enter student name: ")
roll_number = int(input("Enter roll number: "))
attendance_count = int(input("Enter attendance count: "))

# Logic:
class Student:
    def __init__(self, student_name, student_roll_number):
        self.name = student_name
        self.roll_number = student_roll_number
        self.attendance = 0

    def introduce(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}"

    def mark_attendance(self):
        self.attendance += 1

    def attendance_summary(self):
        return f"{self.name} attended {self.attendance} classes"


student = Student(name, roll_number)
for _ in range(attendance_count):
    student.mark_attendance()

# Output:
print(student.introduce())
print(student.attendance_summary())
