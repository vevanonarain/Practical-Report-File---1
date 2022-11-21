# Task 18 - 03/08/2022
""" Write a Python program to input two natural numbers and check whether those
    numbers are amicable or not. """
# Vevan O Narain S6- C


def sumOfDivisors(x):
    sum = 1

    for i in range(2, x):
        if (x % i == 0):
            sum += i

    return sum


def isAmicable(a, b):
    if (sumOfDivisors(a) == b and sumOfDivisors(b) == a):
        print(f"{a} and {b} are amicable numbers.")
    else:
        print(f"{a} and {b} are not amicable numbers.")


num1 = int(input("Enter the first natural number: "))
num2 = int(input("Enter the second natural number: "))
isAmicable(num1, num2)
