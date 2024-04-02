# def whhichCake(ingredients, base, coating):
#   if ingredients == "chocolate":
#     print("Mmm, chocolate cake is amazing")
#   elif ingredients == "broccoli":
#     print("You what mate?!")
#   else:
#     print("Yeah, that's great I suppose...")
#   print("So you want a", ingredients, "cake on a", base, "base with", coating,)

# userIngr = input("Name an ingredient: ")
# userBase = input("Name a type of base: ")
# userCoat = input( "Fave cake topping: ")
# whhichCake(userIngr, userBase, userCoat)

print()
import random
print("Infinity Dice ")

sides = int(input("How many sides?: "))

playGame = "yes"

def rollDice(sides):
  print("You rolled ", random.randint(1,sides))
while playGame == "yes":
  rollDice(sides)
  playGame = input("Roll again? ")
    