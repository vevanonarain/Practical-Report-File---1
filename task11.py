# Task 11 - 02/08/2022
""" Write a Python program to input electric consumption of a house and
    calculate total electric bill. """
# Vevan O Narain S6- C

while True:
    try:
        print("Calculate Electricity Bill\n")
        units = float(input("Enter the electric units consumed: "))

        if (units <= 200):
            bill = 0

        elif (units <= 400):
            bill = units * 4.5

        elif (units <= 800):
            bill = units * 6.5

        elif (units <= 1200):
            bill = units * 7

        else:
            bill = units * 7.75

        print(f"Your payable electricity bill is {bill} INR.")

    except ValueError:
        print("Invalid input!")
        continue

    else:
        break
