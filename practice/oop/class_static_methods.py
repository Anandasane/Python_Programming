# Problem Statement:
# Write a Python program to demonstrate instance, class, and static methods.
#
# Intuition:
# Instance methods use object data, class methods use class data, and static methods do not need object or class data.
#
# Input:
value = int(input("Enter a value: "))

# Logic:
class MathUtils:
    multiplier = 10

    def __init__(self, number):
        self.value = number

    def instance_method(self):
        return self.value + 1

    @classmethod
    def class_method(cls, number):
        return number * cls.multiplier

    @staticmethod
    def static_method(number):
        return number**2


utils = MathUtils(value)
instance_result = utils.instance_method()
class_result = MathUtils.class_method(value)
static_result = MathUtils.static_method(value)

# Output:
print(f"Instance method result: {instance_result}")
print(f"Class method result: {class_result}")
print(f"Static method result: {static_result}")
