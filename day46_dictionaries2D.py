john = {"daysCompleted": 46, "streak": 22}
janet = {"daysCompleted": 21, "streak": 21}
erica = {"daysCompleted": 75, "streak": 6}

courseProgress = {"John":john, "Janet":janet, "Erica":erica}
# esto se veria como una lista dentro de otra lista

print(courseProgress["Erica"])
# The bracket contains the key that references the sub dictionary.


print(courseProgress["Erica"]["daysCompleted"])
# bueno con esto accede a los valores o datos de la subdiccionario


clue = {}

def prettyprint():
  print()
  for key, value in clu.items():
      print(key, end=": ") # el original es print(key, value) pero lo pongo asi para que se vea más bonito
      for subkey, subvalue in value.items(): # este for es para que se vea más bonito y que busque dentro del 1er diccionario
          print(subkey, subvalue, end=" | ")
      print()

while True:
  name = input("Name: ")
  location = input("Location: ")
  weapon = input("Weapon: ")
  clue[name] = {"location": location, "weapon": weapon}
  print(clue)

    break

# ---------------------  CHALLENGE --------------------

# 🌟MokeBeast Generator🌟
# Input the beast name > PikaWho?
# Input the beast element > Air
# Input the beast special move > Shaved fish
# Input the beast starting HP > 50
# Input the beast starting MP > 50
# Again? y/n > n
# name: PikaWho? |  element: Air  |  special move: Shaved Fish  |  HP: 50  | MP: 50

mokeBeast = {}

def prettyprint():
  print(f"Name\tElement\tWeapon\tHP\tMP")
  for key, value in mokeBeast.items():
      print(f"""{key:^5}|{value["element"]:^8}|{value["weapon"]:^8}|{value["hp"]:^3}|{value["mp"]:^2}""") 
      

while True:
  name = input("Name beast > ").title()
  element = input("Element > ").title()
  specialMove = input("Weapon > ")
  hp = int(input("HP > "))
  mp = int(input("MP >  "))
  
  mokeBeast[name] = {"element": element, "weapon": specialMove, "hp": hp, "mp": mp}
  prettyprint()
  print()
  
  aga = input("Again? yes/no: ")
  if aga == "yes":
    print()
    continue
  else:
    break
  print()  