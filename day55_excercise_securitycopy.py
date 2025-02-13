# excercise: get the todo list with autosave and autoload from day 51 and before auto saving, create a backup folder, create a random file name and and save a copy of that file to that folder first
# (vamos a coger la tarea pendiente de realizar del dia 51 y antes del auto-guardado, vamos a crear una carpeta con un nombre de archivo aleatorio y guardar una copia de ese archivo a esa carpeta primero)
# basicamente hacer una copia de seguridad

import os, time, random
todo = []
fileExists = True

try:
  f= open("to.do", "r")
  todo = eval(f.read())
  f.close()
except:
  fileExists = False



def add():
  time.sleep(1)
  os.system("clear")
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Added")

def view():
  time.sleep(1)
  os.system("clear")
  options = input("1: All\n2: By Priority\n> ")
  if options=="1":
    for row in todo:
      for item in row:
        print(item, end=" | ")
      print()
    print()
  else:
    priority = input("What priority? > ").capitalize()
    for row in todo:
      if priority in row:
        for item in row:
          print(item, end=" | ")
        print()
    print()
  time.sleep(1)

def edit():
  time.sleep(1)
  os.system("clear")
  find = input("Name of todo to edit > ")
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
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Added")

def remove():
  time.sleep(1)
  os.system("clear")
  find = input("Name of todo to remove > ")
  for row in todo:
    if find in row:
      todo.remove(row)

while True:
  menu = input("1: Add\n2: View\n3: Edit\n4: Remove\n> ")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  elif menu == "3":
    edit()
  else:
    remove()


  time.sleep(1)
  os.system("clear")

  if fileExists:
    try:
        os.mkdir("backups")
    except:
      pass
    #name = f"backup {random.randint(1, 1000000000)}.txt"
    #os.popen(f"to.do backups/{name}")

    
    name = os.path.join(f"backups/", f"backup nº{random.randint(1, 100)}.txt") #creo una variable name en la que nos crea una copia random y la mete dentro de la carpeta backup
    f = open(name, "w")
    f.close()


  f = open("to.do", "w")
  f.write(str(todo))
  f.close()

