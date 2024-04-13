# myList = []

# def printList():
#   print()
#   for i in myList:
#     print(i)
#   print()

# while True:
#   addItem = input("Item > ")
#   if addItem not in myList:
#     myList.append(addItem) 
#   printList()

#------------------------------------------------------------

# myList = []

# def printList():
#   print()
#   for i in myList:
#     print(i)
#   print()

# # .strip() lo que hace es que ignora los espacios en blanco que le metas al mensaje 
# # .capitalize() lo que hace es que pone la primera letra en mayuscula

# while True:
#   addItem = input("Item > ").strip().capitalize()
#   if addItem not in myList:
#     myList.append(addItem)
#   printList()

# ............ EXERCISE .............
"""
In this exercise you have to put ur name and surname in a list, dont allow duplicated 
using .lower() .strip() .capitalize()
"""
nameList = []
def list():
  print()
  for i in nameList:
    print(i)
  print()

while True:
  addName = input("What is ur Name? ").strip().capitalize()
  addSurname = input("What is your Surname? ").strip().capitalize()
  i=f"{addName} {addSurname}"
  
  if i not in nameList:
    nameList.append(i)

  else:
    print("ERROR: Duplicate name")
  
  list()
  print()
  
  
    
  