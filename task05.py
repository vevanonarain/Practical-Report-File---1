# Task 05 - 01/08/2022
""" Write a Python program to calculate area of circle, rectangle & triangle
    based on user's choice (menu driven). """
# Vevan O Narain S6- C

shape = '0'
area = 0

while True:
    print("Calculate Shape Area\n")
    print("1. Circle\n2. Rectangle\n3. Triangle\n4. Quit\n")
    shape = input("Enter your choice: ")

    if (shape == '1'):
        pi = 3.141592653589793
        radius = float(input("Enter the radius: "))
        area = pi * radius ** 2
        print(f"The area of the circle is {area}.\n")

    elif (shape == '2'):
        length = float(input("Enter the length: "))
        breadth = float(input("Enter the breadth: "))
        area = length * breadth
        print(f"The area of the rectangle is {area}.\n")

    elif (shape == '3'):
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        area = 0.5 * base * height
        print(f"The area of the triangle is {area}.\n")

    elif (shape == '4'):
        break

    else:
        print("Invalid choice!\n")
