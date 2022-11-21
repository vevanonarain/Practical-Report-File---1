# Task 28 - 05/08/2022
""" Write a Python program to input a natural number and display the same but
    after reversing its digits. """
# Vevan O Narain S6- C
try:
    n = input("Enter a number: ")
    print(f"Reversed Number: {int(n[::-1])}")
except:
    print("Invalid Value")