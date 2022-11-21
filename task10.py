# Task 10 - 02/08/2022
""" Write a Python program to input annual income of a person and calculate the
    payable income tax. """
# Vevan O Narain S6- C

while True:
    try:
        print("Calculate Income Tax\n")
        income = int(input("Enter your income in INR: "))

        if (income <= 250000):
            tax = 0

        elif (income <= 500000):
            tax = (income - 250000) * 0.05

        elif (income <= 750000):
            tax = (income - 500000) * 0.10 + 12500

        elif (income <= 1000000):
            tax = (income - 750000) * 0.15 + 37500

        elif (income <= 1250000):
            tax = (income - 1000000) * 0.20 + 75000

        elif (income <= 1500000):
            tax = (income - 1250000) * 0.25 + 125000

        else:
            tax = (income - 1500000) * 0.30 + 187500

        print(f"Your payable income tax is {tax} INR.")

    except ValueError:
        print("Invalid input!")
        continue

    else:
        break
