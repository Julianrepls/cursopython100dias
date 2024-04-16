myString = "Hello there my friend."
print(myString[0])

# This code outputs the 'H' from 'Hello'

myString = "Hello there my friend."
print(myString[6:11]) 
# esto nos muestra desde la posicion 6 hasta la 11

print(myString[:11])
# This code outputs 'Hello there'.(muestra desde la posicion 0 hasta la 11)

print(myString[12:])
# This code outputs 'my friend.'. (Muestra desde la posicion 12 hasta el final)

print(myString[:])
# This code outputs 'Hello there my friend.'  (muestra todo el texto)

print(myString[0:6:2])
# This code outputs 'Hlo' (every second character from 'Hello').

myString = "Hello there my friend."
print(myString[::3])
# This code outputs 'Hltrmfe!' (every third character from the whole string).
#te va a mostrar una letra cada 3

myString = "Hello there my friend."
print(myString[::-1])
#This code reverses the string, outputting '.dneirf ym ereht olleH'
#te pone el texto del revés

myString = "Hello there my friend."
print(myString.split())
#This code outputs ['Hello', 'there', 'my', 'friend.']
#te forma una lista, está genial porque si no sabes cuantas palabras tiene una frase, puedes separarlas con el split

# myString = "Hello there my friend."
# print(myString[0:4:0])
#esto daría error porque el 0 en el tercer argumento no es un numero valido ya que se va a mover en 0 posiciones todo el rato por tanto no imprime
#el valor que pongamos en el tercer argumento es lo que va a mover con esa frecuencia

# -------------- Excercise --------------

# Ask the user to input their first & last names.
# Slice the first 3 letters of the first name.
# Slice the first 3 letters of the last name (surname).
# Join them together. Ideally change the case so that it looks good - think fStrings or .upper()/.lower(). This is the user's Star Wars first name.
# Now ask the user for their mother's maiden name and the city where they were born. (Maiden name is the last name they had before they got married. If you are not sure, make up a last name.)
# Combine the first two letters of the maiden name with the last 3 letters of the city to make the user's Star Wars last name. Remember, fStrings and .upper()/.lower().
# Finally, print them both as part of a sentence.
# 🥳 Extra points for getting all the inputs with just one input command and the split function.


print("STAR WARS NAME GENERATOR")

all = input("Enter your first name, last name, Mum's maiden name and the city you were born in").split()

first = all[0].strip() #esto da el valor 0 de la lista
last = all[1].strip()
maiden = all[2].strip()
city = all[3].strip()

# estos strips son para que no haya espacios en blanco en el nombre

name = f"{first[:3].title()}{last[:3].lower()} {maiden[:2].title()}{city[-3:].lower()}"

print(f"Your Star Wars name is {name}")


# este programa hace que te contstruya un nombre a raiz de que le pongas los datos que te pide y coge las 3 primeras letras de tu nombre y las 3 ultimas de tu apellido, y las 2 primeras de tu madre y las 3 ultimas de tu ciudad


# otra forma de hacerlo sería esta _

print("STAR WARS NAME GENERATOR")
print()

name = input("Enter your first name")
last = input("Enter your last name")
maiden = input("Enter your mum's maiden name")
city = input("Enter the city you were born in")

name = f"{name[:3].title()}{last[:3].lower()} {maiden[:2].title()} {city[-3:].lower()}"

print(f"Your Star Wars name is {name}")
