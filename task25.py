# Task 25 - 04/08/2022
""" Write a Python program to input two natural numbers and calculate and
    display their LCM. """
# Vevan O Narain S6- C

num1 = int(input("Enter first natural number: "))
num2 = int(input("Enter second natural number: "))
hcf = 1

for i in range(2, num1 + 1):
    if (num1 % i == 0 and num2 % i == 0):
        hcf = i

lcm = int((num1 * num2) / hcf)
print(f"The LCM of {num1} and {num2} is {lcm}.")
