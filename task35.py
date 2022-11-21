# Task 35 - 07/08/2022
""" Write a Python program to input a floating number x and a natural number n
    and calculate and display the sum of the cosine series. """
# Vevan O Narain S6- C

x = float(input("Enter a floating number: "))
n = int(input("Enter a natural number: "))
sum = 1


def factorial(n):
    if (n == 0):
        return 1

    return n * factorial(n - 1)


for i in range(1, n + 1):
    if (i % 2 == 0):
        t = (x ** i) / factorial(i)
        sum -= t

print(f"The sum of the cosine series is {sum}.")
