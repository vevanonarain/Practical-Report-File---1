# Task 50 - 14/08/2022
""" Write a Python program to read a list having 10 country names and display
    only those which are 6 or more characters long. """
# Vevan O Narain S6- C

countries = input("Enter Country 1: ")
l = []
l.append(countries)

no_countries = 0
final = []

for i in range(2, 11):
    countries = input(f"Enter Country {i}: ")
    l.append(countries)

for j in l:
    if (len(j) >= 6):
        no_countries += 1
        final.append(j)

if no_countries == 0:
    print("There are no countries which are more than 6 characters")
else:
    print(f"The countries which are more than 6 characters are:", end = '')
   
    print(*final, sep = ", ")