# Task 46 - 13/08/2022
""" Write a Python program to read a name and display the initials as
    M.K.Gandhi. """
# Vevan O Narain S6- C

name = input("Enter your name: ")
list = name.split()

for i in range(len(list) - 1):
    print(list[i][0].upper(), end='.')
print(list[-1].title())
