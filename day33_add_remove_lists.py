# myAgend = []

# def printList():
#     print()
#     for item in myAgend:
#         print(item)
#     print()


# while True:
#     items = input("What u wanna put in the list?: ")
#     myAgend.append(items)
#     printList()

# .-........................................

# myAgend = []

# def printList():
#     print()
#     for item in myAgend:
#         print(item)
#     print()


# while True:
#     menu = input("Add or remove an item to the list?: ")
#     if menu == "add":
#         item = input("What do you to add?: ")
#         myAgend.append(item)  # a commun error is poner al reves: item.append(myAgend)
        
#     elif menu == "remove":
#         item = input("What do you want to remove?: ")
#         if item in myAgend:
#             myAgend.remove(item)
#         else:
#             print(f"\033[31m{item} is not on the list\033[0m")

        
        
#     printList()

# ...........-.......................-...............

# excersice

print()
print(" ==== To do List Manager ====")
print()
myList = []

def printList():
    print()
    for item in myList:
        print(item)
    print()


while True:
    menu = input("Do you want to Add, edit or view the list?: ")
    if menu == "add":
        item = input("What do you to add?: ")
        myList.append(item)  # a commun error is poner al reves: item.append(myAgend)
        print(f"\033[34m{item}\033[0m was added to the list")
        print()
        
    elif menu == "edit":
        item = input("What do you want to remove?: ")
        
        if item in myList:
            myList.remove(item)
            print(f"\033[31m{item} \033[0m was removed")
            print()
        else:
            print(f"\033[35m{item} \033[0m is not on the list")
            print()

    elif menu == "view":
        
        printList()
        print()

    else:
        print("Please chose Add, edit or view")
