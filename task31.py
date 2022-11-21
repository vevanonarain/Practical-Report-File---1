# Task 31 - 07/08/2022
""" Write a Python program to input 3 numbers and display those in ascending/
    descending order. """
# Vevan O Narain S6- C

list = []

for i in range(1, 4):
    num = int(input("Enter a number: "))
    list.append(num)

print()
list.sort()
print("The increasing order of numbers is ", end="")
print(*list, sep=", ", end=".")
print()
list.sort(reverse=True)
print("The decreasing order of numbers is ", end="")
print(*list, sep=", ", end=".")
print()
