import os, time
inventory = []

try:
    f = open("inventory.txt", "r")
    inventory = eval(f.read())
    f.close()
except:
    pass

def addItem():
    time.sleep(1)
    os.system("clear")
    item = input("Item to add > ").capitalize()
    inventory.append(item)
    print("Added")

def removeItem():
    time.sleep(1)
    os.system("clear")
    item = input("Item to remove> ").capitalize()
    if item in inventory:
        inventory.remove(item)
        print("Item REMOVED")
    else:
        print("You dont have that item")

def viewItem():
    time.sleep(1)
    os.system("clear")
    for item in inventory:
        print(f"{item} {inventory.count(item)}")
    
    time.sleep(2)

while True:
    time.sleep(1)
    os.system("clear")
    print()
    print("---= INVENTORY =---")
    menu = input("Add: 1\nRemove: 2\nView: 3\n>")
    if menu == "1":
        addItem()
    elif menu == "2":
        removeItem()
    else:
        viewItem()

    f = open("inventory.txt", "w")
    f.write(str(inventory))
    f.close()



