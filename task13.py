# Task 13 - 02/08/2022
""" Write a Python program to input a natural number and display the
    multiplication table of that number. """
# Vevan O Narain S6- C

n = int(input("Enter a natural number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
