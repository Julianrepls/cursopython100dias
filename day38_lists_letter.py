vowels = ["a", "e", "i", "o", "u"]

#lo que hacemos con esto es que vuelve el texto que escribamos con las vocales de la lista en color amarillo
myString = input("Type somethin: ")
for letter in myString:
  if letter.lower() in vowels:
    print('\033[33m', end='')  #yellow #el end es para que no se salte de linea
  print(letter, end="")
  print('\033[0m', end='')  # vuelve el texto a por defecto

#--------------------------------------------------------------------

myString = "Day 38"
for letter in myString:
  if letter.lower() == "a":
    print('\033[33m', end='')  #yellow
  print(letter)
  print('\033[0m', end='')  #back to default

# This code outputs (with a yellow 'a'):
#D
#a
#y

#3
#8

voweList = ["a", "e", "i", "o", "u"]

myString = input("Type somethin: ")
for letter in myString:
  if letter.lower() in voweList:
    print('\033[33m', end='')  #yellow #el end es para que no se salte de linea
  print(letter, end="")
  print('033[0m', end='')  # vuelve el texto a por defecto

#----------- Exercise --------------

# 1. Ask the user to input any sentence (string).
# 2. Now we'll rainbow-ize (nope, me neither) it.
# 3. As soon as the string contains an 'r', every letter from that point on should be red.
# 4. When the computer encounters a 'b', 'g', 'p' or 'y', from there the output should be blue for 'b', green for 'g'...you get the idea.
# 5. Loop through the string and output it (so the color continues through the loop).
# 6. The output should change color every time it encounters a new r,g,b,p or y.
# 🥳 Extra points for resetting the output color back to default every time there's a space.


def colorChange(color):
  if color == "r":
    print("\033[31m", end="")
  elif color == " ":
    print("\033[0m", end="")
  elif color == "b":
    print("\033[34m", end="")
  elif color == "y":
    print("\033[33m", end="")
  elif color == "g":
    print("\033[32m", end="")
  elif color == "p":
    print("\033[35m", end="")


# Esto te lee cada letra de la frase y va chequeando según la funcion def colorChange

sentence = input("What sentence do you want rainbow-izing?: ")
for letter in sentence:
  colorChange(letter.lower())
  print(letter, end="")
print()
