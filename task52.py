# Task 52 - 15/08/2022
""" Write a Python program to read a list having 10 names and display only
    those which end with consonants. """
# Vevan O Narain S6- C

l = []

for i in range(1, 11):
    names = input(f"Enter Name {i}: ")
    l.append(names)

print("Names which end in consonants: ")

for name in l:
    if (name[-1].upper() not in 'AEIOU'):
        print(name)
