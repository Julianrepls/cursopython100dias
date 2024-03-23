# print("contador")
# counter = 0
# while counter < 12:
#   print(counter)
#   counter +=1
# print("fin")

# animal = ""

# while animal == "":
#   animal = input("¿what animal do u want to hear? Cow, dog, cat, or duck?: ")
#   if animal.lower() == "exit":
#     break
#   elif animal.lower() == "cow":
#     print("Moo")

#   elif animal.lower() == "dog":
#     print("Woof")

#   elif animal.lower() == "cat":
#     print("Meow")

#   elif animal.lower() == "duck":
#     print("Quack")

#   else:
#     print("I don't know that animal")


# exit = "no"

# while exit == "no":
#   animal = input("¿what animal do u want to hear? Cow, dog, cat, or duck?: ")
#   if animal.lower() == "exit":
#     break
#   elif animal.lower() == "cow":
#     print("Moo")

#   elif animal.lower() == "dog":
#     print("Woof")

#   elif animal.lower() == "cat":
#     print("Meow")

#   elif animal.lower() == "duck":
#     print("Quack")

#   else:
#     print("I don't know that animal")

#   exit = input("¿do u want to exit?: ")

exit = "no"
print("Si quieres salir escribe exit")
while exit == "no":
  animal = input("¿what animal do u want to hear? Cow, dog, cat, or duck?: ")
  
  if animal.lower() == "exit":
    break
  if animal.lower() == "cow":
    print("Moo")

  elif animal.lower() == "dog":
    print("Woof")

  elif animal.lower() == "cat":
    print("Meow")

  elif animal.lower() == "duck":
    print("Quack")

  else:
    print("I don't know that animal")

  exit = input("¿do u want to exit?: ")
  if exit.lower() != "no":
      print("has salido")

    
    

  
   