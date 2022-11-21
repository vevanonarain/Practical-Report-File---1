# Task 21 - 04/08/2022
""" Write a Python program to input a number n and display all prime numbers
    less than equal to n. """
# Vevan O Narain S6- C


def isPrime(n):
    if (n < 2):
        return False

    if (n <= 3):
        return True

    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5

    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6

    return True


def printPrime(n):
    for i in range(2, n + 1):
        if isPrime(i):
            print(i, end=" ")


n = int(input("Enter a natural number: "))
printPrime(n)
