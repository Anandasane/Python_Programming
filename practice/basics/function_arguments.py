# Problem Statement:
# Write a Python program to demonstrate positional, default, keyword, and arbitrary arguments.
#
# Intuition:
# Functions can accept required values, default values, named values, and extra keyword values.
#
# Input:
name = input("Enter name: ")
greeting = input("Enter greeting or press Enter for default: ")
age = int(input("Enter age: "))
city = input("Enter city or press Enter for default: ")
language = input("Enter programming language: ")
level = input("Enter skill level: ")

# Logic:
if greeting.strip() == "":
    greeting = "Hello"
if city.strip() == "":
    city = "Unknown"


def greet(person_name, person_greeting="Hello"):
    return f"{person_greeting}, {person_name}!"


def describe_person(person_name, person_age, person_city="Unknown"):
    return {"name": person_name, "age": person_age, "city": person_city}


def build_profile(person_name, **details):
    profile = {"name": person_name}
    profile.update(details)
    return profile


greeting_message = greet(name, greeting)
person_details = describe_person(name, age, city)
profile = build_profile(name, language=language, level=level)

# Output:
print(greeting_message)
print(f"Person details: {person_details}")
print(f"Profile: {profile}")
