# Task 24 - 04/08/2022
""" Write a Python program to input two natural numbers and check whether they
    are co-prime or not. """
# Vevan O Narain S6- C


def areCoprime(a, b):
    hcf = 1

    for i in range(1, a + 1):
        if (a % i == 0 and b % i == 0):
            hcf = i
            print(f"{a} and {b} are co-prime.")
        else:
            return (hcf == 1)
            print(f"{a} and {b} are not co-prime.")


num1 = int(input("Enter the first natural number: "))
num2 = int(input("Enter the second natural number: "))
areCoprime(num1, num2)
