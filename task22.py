# Task 22 - 04/08/2022
""" Write a Python program to input a natural number n and display the sum of
    all prime numbers less than equals to that number n. """
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


def sumOfPrimes(n):
    sum = 0

    for i in range(2, n + 1):
        if isPrime(i):
            sum += i

    print(sum)


n = int(input("Enter a natural number: "))
print(f"The sum of first prime numbers less than or equal to {n}: ")
sumOfPrimes(n)
