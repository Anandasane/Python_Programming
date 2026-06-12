# Problem Statement:
# Write a Python program to demonstrate abstraction using a payment interface.
#
# Intuition:
# Abstraction hides implementation details and exposes only the required method.
#
# Input:
payment_method = input("Enter payment method (credit_card/upi): ")
amount = float(input("Enter amount: "))

# Logic:
from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, value):
        pass


class CreditCardPayment(Payment):
    def pay(self, value):
        return f"Paid {value} using credit card"


class UPIPayment(Payment):
    def pay(self, value):
        return f"Paid {value} using UPI"


if payment_method == "credit_card":
    payment = CreditCardPayment()
else:
    payment = UPIPayment()

# Output:
print(payment.pay(amount))
