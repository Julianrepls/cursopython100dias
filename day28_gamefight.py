import random, os, time


def rollDice(sides):
  total = random.randint(1, sides)
  return total


def health():

  healthstat = ((rollDice(6)*rollDice(12))/2)+10
  return healthstat


def strength():
  strengthstat = ((rollDice(6)*rollDice(8))/2)+12
  return strengthstat



            # campeón 1
  
print(" --- BATTLE ---")
character = input("Name Character?:\n")
time.sleep(1)
  
character_type = input("Select type: Human, Elf, Trol, Wizard, Orc:\n")
time.sleep(1)
  
print("Good! You picked: ", character, "the ", character_type)
time.sleep(1)

print()
            # estadísticas campeón 1
  
char1_health = health()
st1_strenght = strength()
print("HEALTH: ", char1_health)
time.sleep(1)
print("STRENGTH", st1_strenght)
time.sleep(1)

            # campeón número 2

character2 = input("Create other Character to fight with> \n ")
time.sleep(1)
character_type2 = input("Select type: Human, Elf, Trol, Wizard, Orc:\n")
time.sleep(1)
print("Good! You picked: ", character2, "the ", character_type2)
time.sleep(1)

print()
            
            # estadísticas campeón 2

char2_health = health()
st2_strenght = strength()
print("HEALTH: ", char2_health)
time.sleep(1)
print("STRENGTH", st2_strenght)
time.sleep(1)


print()

round = 1
winner = None

while True:
  time.sleep(1)
  os.system ("clear")
  print(" --- BATTLE ---")

  c1Dice = rollDice(6)
  c2Dice = rollDice(6)

  difference = abs(st1_strenght - st2_strenght) + 1  # la función abs devuelve un valor positivo siempre
    
  if c1Dice > c2Dice:
    char2_health -= difference
    if round == 1:
      print(character, "wins the 1 rst")
    else: 
      print(character, "wins round", round)
    
  elif c2Dice > c1Dice:
    char1_health -= difference
    if round == 1:
      print(character2, "wins the 1 rst")
    else:
      print(character2, "wins round", round)

  else: 
    print("They tie", round)

  print()
  print(character)
  print("Health", char1_health)
  print()
  print(character2)
  print("Health", char2_health)

  if char1_health <= 0:
    print(character, "is death")
    winner = character2
    break
  elif char2_health <= 0:
    print(character2, "is death") 
    winner = character
    break
  else:
    print("The both are ready for the next round")
    round +=1

time.sleep(1)
os.system("clear")
print()
print(winner, "has won in", round, "rounds")

