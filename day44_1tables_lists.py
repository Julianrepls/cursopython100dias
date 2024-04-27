list = []

while True:
  name = input("what is your name? ")
  age = input("what is your age? ")
  pref = input("what is your computer platform? ")
  row = [name, age, pref]
  list.append(row)
  exit = input("exit? ")
  if (exit.strip().lower()[0] == "yes"): 
    break
    
print(list)  
#///////// explicación

listOfShame = [] 
# Creates an empty list.

while True: 
  # Starts a never ending loop (until we end it)
  name = input("What is your name? ")
  age = input("What is your age? ")
  pref = input("What is your computer platform? ")
  # Get the user input.

  row = [name, age, pref] 
  # Assigns the 3 variables into a single row.

  listOfShame.append(row) 
  # Adds the contents of the row variable at the end of the list

  exit = input("Exit? y/n") 
  # Get user choice to quit, yes or no?

  if (exit.strip().lower()[0] == "y"): 
    # strip removes unwanted spaces from the input. lower()[0] makes sure the first character of the input is lower case so it can be compared to 'y'
    break # break ends a loop and jumps to the next line of code that is not part of the loop.

print(listOfShame) # Outputs the list. Note this is NOT part of the loop (not indented), it only runs once the loop ends.









#///////// con este Def prettyPtrint() vamos a hacer que nos muestre las filas agregadas pero en forma de listas, es decir, con los corchetes
#  comilla simple:


def prettyPrint():
  print() 
  # fila en blanco en top
  for row in listOfShame: 
    # esto recorre cada fila de la lista
     print(row) 
    # esto muestra las filas
  print() 
  # prints una fila en blanco entre filas



#//////// con el Def definitelyPrint() vamos a hacer que nos muestre las filas y los items pero ya sin los corchetes y las comillas
# además con la fución de encadenar f"" vamos a hacer que aparezca como una tabla.
# mostraria esto:

#    juli     |      34      |     win      |          
#    paco     |      40      |     mac      |          


def definitelyPrint():
  print() 
  for row in listOfShame: 
    for item in row: 
    # esto recorre cada item de cada columna de cada fila
      print(f"{item:^10}", end=" | ") 
    # :^10 means 10 characters as the space with the data in the center. The end character has been changed to space vertical line space to make it look more like a table. En definitiva lo muestra centrado y con espacio entre cada item con la barra asemejándose a una tabla.
    print()

  print() 




listOfShame = [] 

while True: 
  name = input("What is your name? ")
  age = input("What is your age? ")
  pref = input("What is your computer platform? ")

  row = [name, age, pref] 

  listOfShame.append(row) 

  exit = input("Exit? y/n: ") 

  if (exit.strip().lower()[0] == "y"):
    break 

definitelyPrint() 
# Call the definitelyPrint subroutine instead of printing the list directly.


# //////// Ahora para eliminar FILA de la lista:

listOfShame = []

def prettyPrint():
  for row in listOfShame:
    for item in row:
      print(f"{item:^10}", end=" | ")
    print()

while True:
  menu = input("Add or Remove? ")

  if (menu.strip().lower()[0] == "a"):
    
  
    name = input("Whats your name? ")
    age = input("Whats your age? ")
    pref = input("Whats your computer platform? ")
  
    row = [name, age, pref]
  
    listOfShame.append(row)
    
    prettyPrint()
  
  else:
    name = input("Name to remove_ ")
    for row in listOfShame:
      if name in row:
        listOfShame.remove(row)
    print()
    prettyPrint()


