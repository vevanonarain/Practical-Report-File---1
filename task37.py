# Task 37 - 07/08/2022
""" Write a Python program to input a natural number n (if n = 4) and display
    the pattern: *
                 * *
                 * * *
                 * * * *. """
# Vevan O Narain S6- C

n = int(input("Enter a natural number: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print('*', end="")
    print()
