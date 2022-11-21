# Task 49 - 14/08/2022
""" Write a Python program to read a sentence and check whether that sentence
    contains a word entered by the user (with or without case sensitivity). """
# Vevan O Narain S6- C

word = input("Enter a word: ")
str = input("Enter a sentence: ")

if (word.lower() in str.lower()):
    print(f"The sentence '{str}' contains {word}.")
else:
    print(f"The sentence '{str}' does not contain {word}.")
