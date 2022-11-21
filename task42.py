# Task 42 - 11/08/2022
""" Write a Python program to process following menu based operations on a list
    having numbers: Create, Append, Display, Search, Modify, Delete. """
# Vevan O Narain S6- C

choice = '0'
list = []

while True:
    print("List Operations\n")
    print("1. Create\n2. Append\n3. Display\n4. Search\n5. Modify\n6. Delete\
\n7. Quit\n")
    choice = input("Enter your choice: ")

    if (choice == '1'):
        print("The list has been created.\n")

    elif (choice == '2'):
        element = float(input("Enter the element to pushed: "))
        list.append(element)
        print(f"{element} has been pushed into the list.\n")

    elif (choice == '3'):
        if (len(list) > 0):
            print(f"The list is {list}.\n")
        else:
            print("List is empty!\n")

    elif (choice == '4'):
        element = float(input("Enter the element to be searched: "))
        if (element in list):
            print(f"{element} is in the list.\n")
        else:
            print(f"{element} is not in the list.\n")

    elif (choice == '5'):
        method = '0'

        while True:
            print("List Modify Operations\n")
            print("1. Clear\n2. Reverse\n3. Sort\n4. Quit\n")
            method = input("Enter your choice: ")

            if (method == '1'):
                list.clear()
                print("The list has been cleared.\n")

            elif (method == '2'):
                list.reverse()
                print("The list has been reversed.\n")

            elif (method == '3'):
                list.sort()
                print("The list has been sorted.\n")

            elif (method == '4'):
                break

            else:
                print("Invalid choice!\n")

    elif (choice == '6'):
        if (len(list) > 0):
            element = float(input("Enter the element to be popped: "))
            list.remove(element)
            print(f"{element} has been popped from the list.")
        else:
            print("UNDERFLOW! List is empty. Deletion is NOT possible.\n")

    elif (choice == '7'):
        break

    else:
        print("Invalid choice!\n")
