# Task 38 - 08/08/2022
""" Write a Python program to input a natural number n (if n = 4) and display
    the pattern: 1
                 1 2
                 1 2 3
                 1 2 3 4. """
# Vevan O Narain S6- C

n = int(input("Enter a natural number: "))

for i in range(2, n + 2):
    for j in range(1, i):
        print(j, end="")
    print()
