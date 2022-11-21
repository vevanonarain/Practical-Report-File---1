# Task 15 - 03/08/2022
""" Write a Python program to input a natural number and display all the
    factors of that number. """
# Vevan O Narain S6- C

n = int(input("Enter a natural number: "))
factors = []

for i in range(1, n + 1):
    if (n % i == 0):
        factors.append(i)

print(f"The factors of {n} are {factors}.")
