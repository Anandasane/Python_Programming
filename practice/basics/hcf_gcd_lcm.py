# Problem Statement:
# Write a Python program to find HCF, GCD, and LCM of two numbers and a list of numbers.
#
# Intuition:
# HCF and GCD are the same. Euclid's algorithm repeatedly replaces the larger number with the remainder until the remainder becomes zero. LCM is found using (a * b) / HCF.
#
# Input:
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
numbers_input = input("Enter numbers separated by spaces to find HCF and LCM: ")

# Logic:
def hcf(a, b):
    first = abs(a)
    second = abs(b)
    while second != 0:
        first, second = second, first % second
    return first


def gcd(a, b):
    return hcf(a, b)


def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // hcf(a, b)


def hcf_of_list(values):
    result = values[0]
    for value in values[1:]:
        result = hcf(result, value)
    return result


def lcm_of_list(values):
    result = values[0]
    for value in values[1:]:
        result = lcm(result, value)
    return result


numbers = [int(value) for value in numbers_input.split()]
hcf_result = hcf(first_number, second_number)
gcd_result = gcd(first_number, second_number)
lcm_result = lcm(first_number, second_number)
list_hcf = hcf_of_list(numbers)
list_lcm = lcm_of_list(numbers)

# Output:
print(f"HCF of {first_number} and {second_number}: {hcf_result}")
print(f"GCD of {first_number} and {second_number}: {gcd_result}")
print(f"LCM of {first_number} and {second_number}: {lcm_result}")
print(f"HCF of {numbers}: {list_hcf}")
print(f"LCM of {numbers}: {list_lcm}")
