# Task 12 - 02/08/2022
""" Write a Python program to input two natural numbers and display all the
    even numbers between them. """
# Vevan O Narain S6- C

x = int(input("Enter first natural number: "))
y = int(input("Enter second natural number: "))
even = []
no_even = 0

for i in range(x + 1, y):
    if (i % 2 == 0):
        even.append(i)
        no_even += 1

if no_even >= 1:
    print(f"Even numbers between {x} and {y} are ", end="")
    print(*even, sep=", ", end=".")
else:
    print(f"There are no even numbers between {x} and {y}")