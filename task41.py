# Task 41 - 09/08/2022
""" Write a Python program to illustrate the difference between append() and
    insert() methods and pop() and remove() methods when applied on a list. """
# Vevan O Narain S6- C

choice = '0'
list = []

while True:
    print("List Operations\n")
    print("1. Append\n2. Insert\n3. Pop\n4. Remove\n5. Quit\n")
    choice = input("Enter your choice: ")

    if (choice == '1'):
        element = input("Enter the element to appended: ")
        list.append(element)
        print(f"The list is {list}.\n")

    elif (choice == '2'):
        element = input("Enter the element to inserted: ")
        list.insert(0, element)
        print(f"The list is {list}.\n")

    elif (choice == '3'):
        if (len(list) > 0):
            list.pop()
            print(f"The list is {list}.\n")
        else:
            print("UNDERFLOW! List is empty. Deletion is NOT possible.\n")

    elif (choice == '4'):
        if (len(list) > 0):
            element = input("Enter the element to be removed: ")
            list.remove(element)
            print(f"The list is {list}.\n")
        else:
            print("UNDERFLOW! List is empty. Deletion is NOT possible.\n")

    elif (choice == '5'):
        break

    else:
        print("Invalid choice!\n")
