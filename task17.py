# Task 17 - 03/08/2022
""" Write a Python program to input a natural number and check whether the
    number is a perfect or not. """
# Vevan O Narain S6- C

num = int(input("Enter a natural number: "))
sum = 0

for i in range(1, num):
    if (num % i == 0):
        sum += i

if (sum == num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
