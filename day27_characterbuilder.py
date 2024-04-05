print()
"""
Write a subroutine that generates a character: first name and character type (human, imp, wizard, elf, etc.).
Write a subroutine that multiplies a bunch of random dice rolls together to generate the character's health stats. Use this formula:
"""
import random
import os, time


def rollDice(sides):
  total = random.randint(1, sides)
  return total


def roll6():
  roll6 = rollDice(6)
  stat6 = ((roll6 * rollDice(12) / 2) + 10)
  return stat6


def roll8():
  roll8 = rollDice(8)
  stat8 = ((roll8 * rollDice(12) / 2) + 12)
  return stat8


while True:
  
  print(" --- STAT GENERATOR ---")
  character = input("Name Character?:\n")
  print(character, "The Brave")
  time.sleep(1)
  character_type = input("Select type: Human, Elf, Trol, Wizard, Orc:\n")
  time.sleep(1)
  print("Good! You picked: ", character_type)
  time.sleep(1)
  print("ok... rolling dices ...")
  time.sleep(1)
  print("...")
  time.sleep(2)
  
  print()
  
  stat6 = str(roll6())
  stat8 = str(roll8())
  print("HEALTH: ", stat6)
  time.sleep(1)
  print("STRENGTH", stat8)
  time.sleep(1)
  
  character2 = input("Do u want to create other Character?> \n ")
  time.sleep(2)
  if character2 == "no" or character2 == "No":
    print("Thanks for playing! bye")
    break
    
  else: 
    print("lets go again")
    time.sleep(2)
    os.system("clear")
    continue
  
  






# SOLUCION:

# import random, os, time

# def rollDice(side):
#   result = random.randint(1,side)
#   return result

# def health():
#   healthStat = ((rollDice(6)*rollDice(12))/2)+10
#   return healthStat

# def strength():
#   strengthStat = ((rollDice(6)*rollDice(8))/2)+12
#   return strengthStat

# while True:
#   print("⚔️ CHARACTER BUILDER ⚔️")
#   print()
#   name = input("Name your Legend:\n")
#   type = input("Character Type (Human, Elf, Wizard, Orc):\n")
#   print()
#   print(name)
#   print("HEALTH:", health())
#   print("STRENGTH:", strength())
#   print()
#   print("May your name go down in Legend…")
#   print()
#   again = input("Again?:\n")
#   if again=="No" or again=="no":
#     break
#   time.sleep(1)
#   os.system("clear")
