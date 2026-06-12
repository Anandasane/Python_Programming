# Problem Statement:
# Write a Python program to demonstrate encapsulation using a bank account.
#
# Intuition:
# Private variables protect data, and methods control how the data is changed.
#
# Input:
owner = input("Enter account owner name: ")
initial_balance = float(input("Enter initial balance: "))
deposit_amount = float(input("Enter deposit amount: "))
withdraw_amount = float(input("Enter withdraw amount: "))

# Logic:
class BankAccount:
    def __init__(self, account_owner, balance):
        self.owner = account_owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance


account = BankAccount(owner, initial_balance)
account.deposit(deposit_amount)
withdraw_success = account.withdraw(withdraw_amount)

# Output:
print(f"Owner: {account.owner}")
print(f"Balance: {account.get_balance():.2f}")
print(f"Withdraw success: {withdraw_success}")
