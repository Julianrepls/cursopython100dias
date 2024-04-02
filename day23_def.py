def rollDice():
    import random
    dice = random.randint(1,6)
    print(dice)
rollDice()    
print()
print("vamos a tirar el dado 5 veces ahora")
for i in range (5):
    rollDice()
rollDice()    
print()
def login():
  while True:
    username = input("what is ur username?: ")
    password = input("what is ur password?: ")
    if username == "Juli" and password == "1234":
      print("Welcome to my website")
      break
    else:
      print("try again")
print("Login web")
login()
