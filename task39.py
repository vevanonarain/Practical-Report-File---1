# Task 39 - 08/08/2022
""" Write a Python program to input a natural number n (if n = 4) and display
    the pattern:      *
                    * * *
                  * * * * *
                * * * * * * *. """
# Vevan O Narain S6- C

n = int(input("Enter a natural number: "))
str = "*" * n

for i in range(len(str)):
    print(" " * (len(str) - i - 1), end=str[0:i + 1])
    for j in range(1, i + 1):
        print('*', end="")
    print()
