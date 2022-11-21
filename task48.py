# Task 48 - 14/08/2022
""" Write a Python program to read a sentence and display the same by reversing
    characters of all words without changing the sequence of the words. """
# Vevan O Narain S6- C

str = input("Enter a sentence: ")
words = str.split()

for ch in words:
    print(ch[::-1], end=" ")
print()
