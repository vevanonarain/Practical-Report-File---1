# Task 27 - 05/08/2022
""" Write a Python program to input a natural number and check whether the
    number is a Armstrong number or not. """
# Vevan O Narain S6- C

n = int(input("Enter a natural number: "))
arm = n
p = 0

while (n > 0):
    remainder = n % 10
    p += pow(remainder, len(str(abs(arm))))
    n //= 10

if (arm == p):
    print(f"{arm} is an Armstrong number.")

else:
    print(f"{arm} is not an Armstrong number.")
