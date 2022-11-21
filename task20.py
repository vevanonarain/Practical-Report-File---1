# Task 20 - 04/08/2022
""" Write a Python program to input a natural number n and display the first n
    prime numbers. """
# Vevan O Narain S6- C

n = int(input("Enter a natural number: "))
i = 1
count = 0

print(f"First {n} prime numbers are: ")

while (count < n):
    for x in range(i, i + 1):
        factors = 0

        for y in range(1, x + 1):
            if (x % y == 0):
                factors += 1

        if (factors == 2):
            print(f"{x}", end=" ")
            count += 1

    i += 1
