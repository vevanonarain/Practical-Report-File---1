# Task 33 - 07/08/2022
""" Write a Python program to input a floating number x and a natural number n
    and calculate and display the sum of the following series:
        1 ± x + x2 ± x3 + ……… ± xn. """
# Vevan O Narain S6- C
    
x = float(input("Enter a floating number: "))
n = int(input("Enter a natural number: "))
sum = 1

for i in range(n + 1):
    t = pow(x, i) * pow(-1, i)
    sum += t

print(f"The sum of the series is {sum}.")
