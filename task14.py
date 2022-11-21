# Task 14 - 03/08/2022
""" Write a Python program to input a natural number n and display first n
    fibonacci numbers. """
# Vevan O Narain S6- C

a = 0
b = 1
list = [0]
n = int(input("Enter a natural number: "))

for i in range(n - 1):
    c = a + b
    a = b
    b = c
    list.append(c)

print(f"The first {n} Fibonacci numbers are ", end="")
print(*list, sep=", ", end=".")
