# Task 23 - 04/08/2022
""" Write a Python program to input two natural numbers and calculate and
    display their HCF/GCD. """
# Vevan O Narain S6- C

num1 = int(input("Enter first natural number: "))
num2 = int(input("Enter second natural number: "))
hcf = 1

for i in range(2, num1 + 1):
    if (num1 % i == 0 and num2 % i == 0):
        hcf = i

print(f"The HCF/GCD of {num1} and {num2} is {hcf}.")
