# Task 16 - 03/08/2022
""" Write a Python program to input a natural number and display the sum of all
    proper factors."""
# Vevan O Narain S6- C

n = int(input("Enter a natural number: "))
factors = [1]

for i in range(2, n + 1):
    if (n % i == 0):
        factors.append(i)

sum = sum(factors)
print(f"The sum of factors of {n} is {sum}.")
