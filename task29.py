# Task 29 - 05/08/2022
""" Write a Python program to input a natural number and check whether the
    number is palindromic or not. """
# Vevan O Narain S6- C

n = input("Enter a natural number: ")

if (n == n[::-1]):
    print("Number is a palindrome.")

else:
    print("Number is not a palindrome.")
