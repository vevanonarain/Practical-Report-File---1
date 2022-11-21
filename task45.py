# Task 45 - 13/08/2022
""" Write a Python program to read a name and display the initials as M.K.G."""
# Vevan O Narain S6- C

name = input("Enter your name: ")
list = name.split()

for i in list:
    print(i[0].upper(), end='.')
