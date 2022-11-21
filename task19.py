# Task 19 - 04/08/2022
""" Write a Python program to input a natural number and check whether the
    number is a prime or not. """
# Vevan O Narain S6- C


def isPrime(n):
    if (n <= 1):
        print("Invalid input!")

    for i in range(2, n):
        if (n % i == 0):
            return False

    return True


n = int(input("Enter a natural number: "))
print(f"{n} is a prime number.") if isPrime(n) else print(f"{n} is not a prime number.")
