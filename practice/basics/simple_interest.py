# Problem Statement:
# Write a Python program to calculate simple interest.
#
# Intuition:
# Simple interest is calculated as Principal * Rate * Time / 100.
#
# Input:
principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate: "))
time = float(input("Enter time in years: "))

# Logic:
simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

# Output:
print(f"Simple interest: {simple_interest:.2f}")
print(f"Total amount: {total_amount:.2f}")
