"""
Un ejercicio con bucles y def donde se nos pide que metamos una serie de tareas en una lista y luego podamos
añadir más tareas, editarla, mostrarla y eliminarla

"""



# Name | Date | priority

import time
todo = []

def add():
    time.sleep(1)
    # os.system("clear")
    
    name = input("Name_ ")
    date = input("Due Date_ ")
    priority = input("Priority_ ").capitalize()
    row = [name, date, priority]
    todo.append(row)
    print("Added")

def view():
    time.sleep(1)
    # os.system("clear")
    options = input("1: All\n2: By Priority\n_ ")    #recuerda el \n lo que hace es saltar a la linea de abajo, es como darle al intro
    if options =="1":
        for row in todo:
            for item in row:
                print(item, end=" | ")
            print()
        print()
    else: 
        priority = input("What priority?_ ").capitalize()
        for row in todo:
            if priority in row:
                for item in row:
                    print(item, end=" | ")
                print()
        print()
    time.sleep(1)

def edit():
    time.sleep(1)
    # os.system("clear")
    
    find = input("Name of todo to edit_ ")
    found = False
    for row in todo:
        if find in row:
            found = True
    if not found:
        print("Couldn't find that")
        return
    for row in todo:
        if find in row:
            todo.remove(row)
    
    name = input("New Name_ ")
    date = input("Due Date_ ")
    priority = input("Priority_ ").capitalize()
    row = [name, date, priority]
    todo.append(row)
    print("Added")

def remove():
    time.sleep(1)
    # os.system("clear")
    
    find = input("Name of todo to edit_ ")
    
    for row in todo:
        if find in row:
            todo.remove(row)
    
    name = input("Name_ ")
    date = input("Due Date_ ")
    priority = input("Priority_ ").capitalize()
    row = [name, date, priority]
    todo.remove(row)
    print("Added")


while True:
    menu = input("1: Add\n2: View\n3 Edit\n4: Remove\n> ")
    if menu == "1":
        add()
    elif menu == "2":
        view()
    elif menu == "3":
        edit()
    else:
        remove()

    time.sleep(1)
    # os.system("clear")