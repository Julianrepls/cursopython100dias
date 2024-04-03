# def pinPicker(number):
#   import random
#   pin = ""
#   for i in range(number):
#     pin += str(random.randint(0,9))
#   return pin

# myPin = pinPicker(3)
# print(myPin)

print()
import random

def rollDice(sides):
  total = random.randint(1, sides)
  return total

def roll68():
  roll6 = rollDice(6)
  roll8 = rollDice(8)
  stat = roll6*roll8
  return stat

print(" --- STAT GENERATOR ---")
want_character = "yes"

while want_character == "yes":
  character = input("Name Character?: ")
  stat = str(roll68())
  print(character,"have", stat,"hp")
  want_character = input("Do u want to create a Character?_ ")

    