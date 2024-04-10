name = "Katie"
age = "28"
pronouns = "she/her"

print("This is {}, using {} pronouns, and is {} years old.".format(name, pronouns, age))


name = "Katie"
age = "28"
pronouns = "she/her"

print("This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far".format(name=name, pronouns=pronouns, age=age))

print()

name = "Katie"
age = "28"
pronouns = "she/her"

response = "This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far".format(name=name, pronouns=pronouns, age=age)

print(response)

print()
name = "Katie"
age = "28"
pronouns = "she/her"

response = f"This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far"

print()

response = f""""This is {name}, using {pronouns} pronouns, and is {age} years old. 

Hello, {name}. How are you? Have you been having a great {age} years so far"""

print(response)

print ()

for i in range(1, 31):
  print(f"Day {i} of 30")

for i in range(1, 31):
  print(f"Day {i: <2} of 30")  #la diferencia entre este for y el anterior es que ese <2 alinea los carácteres que se van a mostrar en la izquierda, mientras que el <2 del anterior es el número de carácteres que se van a mostrar en la derecha

for i in range(1, 31):
  print(f"Day {i: ^2} of 30")  # (^) esto alinea todo al centro





#excercise:

print("30 Days Down")
print()
for i in range(1, 31):
    think = input(f"What do you think about day {i}?:\n ")
    print()
    myText = f"You though day {i} was {think}"
    
    print(f"{myText: ^35}")
    print(f"{think: ^35}")
    print()