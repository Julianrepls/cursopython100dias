# myEvents = []

# f = open("calendar.txt", "r") # Only need read permissions here
# myEvents = eval(f.read()) 
# f.close()

# def prettyPrint():
#     print()
#     for row in myEvents:
#         print(f'{row[0] :^15} {row[1] :^15}')
#     print()

# while True:
#     menu = input("1: Add, 2: Remove\n")
#     if menu=="1":
#         event =input('What event?: ').capitalize()
#         date = input('What date?: ')
#         row = [event, date]
#         myEvents.append(row)
#         prettyPrint()
#     else:
#         criteria = input('What even do you want to remove?: ').tittle()
#         for row in myEvents:
#             if criteria in row:
#                 myEvents.remove(row)
#         prettyPrint()
    
#     f = open("calendar.txt", "w") # Permissions set to 'w' because we are deleting the file and replacing it with the whole 2D list every time.
#     f.write(str(myEvents)) # Need to cast the list to a single string
#     f.close()



# exercise ---------------------  | Name | Date | Priority |  -----------------------

import os, time
todo = []

f = open("to.do", "r")
todo = eval(f.read())
f.close()

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
  f = open("to.do", "w")
  f.write(str(todo))
  f.close()