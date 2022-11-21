# Task 47 - 13/08/2022
""" Write a Python program to read a string and check whether the string is a
    palindrome or not (with or without case sensitivity). """
# Vevan O Narain S6- C

from re import L


str = input("Enter a string: ")

if (str.lower() == str.lower()[::-1]):
    print("String is a palindrome.")
else:
    print("String is not a palindrome.")
