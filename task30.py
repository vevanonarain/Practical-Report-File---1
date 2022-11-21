# Task 30 - 05/08/2022
""" Write a Python program to input an amount of money and display minimum
    currency notes required to have that money. """
# Vevan O Narain S6- C


def countCurrency(amount):
    notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    notesCount = {}

    for note in notes:
        if (amount >= note):
            notesCount[note] = amount // note
            amount %= note

    print("Currency count: ")

    for key, val in notesCount.items():
        print(f"{key}: {val}")


amount = int(input("Enter the amount: "))
countCurrency(amount)
