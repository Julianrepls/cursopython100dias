import os, random, time

cars = {}

cars["Ferrari"] = {"speed": 97, "acceleration": 90, "braking": 87}
cars["Mercedes"] = {"speed": 92, "acceleration": 78, "braking": 99}
cars["Bugatti"] = {"speed": 95, "acceleration": 92, "braking": 95}
cars["Seat"] = {"speed": 67, "acceleration": 55, "braking": 60}

while True:
  print("-------- TOP WHEELS --------")
  print()
  print("Cars Aviable")
  print()
  for key in cars:
    print(key)
  user = input("Chose your car: Ferrari, Mercdes, bugatti, seat\n>  ")
  time.sleep(2)
  computer = random.choice(list(cars.keys()))
  print()
  print("You picked", user)
  print("Computer picked", computer)
  print()

  attribute = input("Chose your attribute: Speed, acceleration, braking\n>  ")
  print()

  print(f"{user}: {cars[user][attribute]}")
  print(f"{computer}: {cars[computer][attribute]}")
  print()

  if cars[user][attribute] > cars[computer][attribute]:
    print(user, "wins!")
  elif cars[user][attribute] < cars[computer][attribute]:
    print(computer, "wins!")
  else:
    print("It's a draw!")

  os.system("clear")
          
  
  
