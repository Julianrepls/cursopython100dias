"""
en este archivo es un ejemplo de como se hace 
de otra forma este trabajo en concreto y me lo dijo Paco
para que fuera más profesional

"""




import time
toDoList = []

def printList():
  print()
  for items in toDoList:
    print(items)
  print()

while True:
  menu = input("ToDo List Manager\nDo you want to view, add, edit, remove or delete the todo list?\n")
  if menu=="view":
    printList()
  elif menu=="add":
    item = input("What do you want to add?\n").title()
    toDoList.append(item)
  elif menu=="remove":
    item = input("What do you want to remove?\n").title()
    check = input("Are you sure you want to remove this?\n")
    if check[0]=="y":
      if item in toDoList:
        toDoList.remove(item)
  elif menu=="edit":
    item = input("What do you want to edit?\n").title()
    new = input("What do you want to change it to?\n").title()
    toDoList[toDoList.index(item)]=new #esto en concreto es otra forma que me dijo Paco... es mas Pro
    # esta es otra forma de buscar y reemplazar un item de la lista 
    # [new if value == item else value for value in toDoList]   
    

  elif menu=="delete":
    toDoList = []
  time.sleep(1)