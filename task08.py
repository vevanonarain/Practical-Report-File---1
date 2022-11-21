# Task 08 - 01/08/2022
""" Write a Python program to read 3 sides (or angles) of a triangle and
    display the nature of triangle. """
# Vevan O Narain S6- C

a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))

if (a + b > c):
    if (a == b == c):
        print("Triangle is equilateral.")

    elif (a == b or b == c or c == a):
        print("Triangle is isosceles.")

    else:
        print("Triangle is scalene.")

else:
    print("Triangle does not exist!")
