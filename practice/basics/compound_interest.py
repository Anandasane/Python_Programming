# Problem Statement:
# Write a Python program to calculate compound interest.
#
# Intuition:
# Compound interest adds interest to the principal repeatedly over time.
#
# Input:
principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate: "))
time = float(input("Enter time in years: "))
times_compounded = int(input("Enter number of times interest is compounded per year: "))

# Logic:
amount = principal * (1 + rate / (100 * times_compounded)) ** (times_compounded * time)
compound_interest = amount - principal

# Output:
print(f"Compound interest: {compound_interest:.2f}")
print(f"Final amount: {amount:.2f}")
