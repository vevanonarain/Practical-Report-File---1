# Task 44-B - 12/08/2022
""" Write a Python program to read a string and display the following pattern
    if the string is ‘INDIA’:         I
                                    I N
                                  I N D
                                I N D I
                              I N D I A . """
# Vevan O Narain S6- C

n = input("Enter a string: ")

for i in range(len(n)):
    print(" " * (len(n) - i - 1), end=n[0:i + 1])
    print()
