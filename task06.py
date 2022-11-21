# Task 06 - 01/08/2022
""" Write a Python program to solve a quadratic equation and also display the
    nature of roots. """
# Vevan O Narain S6- C

a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant: "))
D = (b**2) - (4*a*c)

if (D > 0):
    root1 = ((-b) + (D)**(1/2))/(2*a)
    root2 = ((-b) - (D)**(1/2))/(2*a)
    print(f"Real and unequal roots are {root1} and {root2}.")

elif (D == 0):
    root = (-b)/(2*a)
    print(f"Real and equal roots are {root} and {root}.")

else:
    print("No real roots exist!")
