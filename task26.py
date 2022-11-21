# Task 26 - 05/08/2022
""" Write a Python program to input a natural number and display the sum of all
    its digits. """
# Vevan O Narain S6- C

n = input("Enter a natural number: ")
sum = 0

try:
    for i in range(0, len(n)):
        sum += int(n[i])
    print(f"The sum of all digits of {n} is {sum}.")

except ValueError:
    print("Invalid input!")
