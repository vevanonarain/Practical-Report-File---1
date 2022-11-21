# Task 07 - 01/08/2022
""" Write a Python program to read a year and check whether the year is a leap
    year or not. """
# Vevan O Narain S6- C

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0):
    print("Year is a leap year.")

else:
    print("Year is not a leap year.")
