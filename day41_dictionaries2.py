myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for i in myDictionary:
  print(myDictionary[i])

myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for value in myDictionary.values():
  print(value)

# //// estas dos funciones no nos devuelve las keys, solo los valores.


# //// esta función si nos devuelve los valores y las keys:
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for name,value in myDictionary.items():
  print(f"{name}:{value}")

#//// esta funcion si te devolveria el valor y la key admás con una condicion
mylist = {"name": "juli", "age": 18, "class": 12}

for name,value in mylist.items():
  print(f"{name}:{value}")

  if (name == "age"):
    print("Wow, that's REALLY OLD")

#//// NOTA: el nombre entre {} con los dos puntos : nos devuelve la clave con su valor, {name}:
#/// por eso hay que poner en el blucle name,value para que nos devuelva la key y el valor

myList = {"name": "juli", "age": 18, "class": 12}
for name, value in myList.items():
  print(f"{name}:{value}")
  if (name == "age"):
    if value >= 18:
      print("You are adult")
    else:
      print(" You are young ")
    



#//// E X E R C I S E

# Create a dictionary that stores the following information about a website: name, URL, description and a star rating (out of 5).
# Use a loop to output the names of the keys, ask the user to type in the details and store the input in the dictionary.
# Finally, output the whole dictionary (keys and values).

webSite = {"name": None, "url": None, "desc": None}

for name, value in webSite.items():
    webSite[name] = input(f"{name}: ")

print()

for name, value in webSite.items():
    print(f"{name}:{value}")
