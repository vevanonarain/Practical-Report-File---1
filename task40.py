# Task 40 - 08/08/2022
""" Write a Python program to input a natural number n (if n = 4) and display
    the pattern:      1
                    1 2 1
                  1 2 3 2 1
                1 2 3 4 3 2 1. """
# Vevan O Narain S6- C

n = int(input("Enter a natural number: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    j = 1

    while (j < i + 1):
        print(j, end="")
        j += 1

    for k in range(j - 2, 0, -1):
        print(k, end="")

    print()
