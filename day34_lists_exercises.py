# import os, time

# listOfEmail = []


# def prettyPrint():
#   os.system("clear") # start by clearing the screen
#   print("listofEmail") # print the title of my program
#   print() 
#   counter=1
  
#   for email in listOfEmail: # use for loop to access list
#     print(f"{counter}: {email}")
#     counter +=1
#   time.sleep(1)

# while True:
#   print("SPAMMER Inc.")
#   menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  
#   if menu == "1":
#     email = input("Email > ")
#     listOfEmail.append(email)
    
#   elif menu =="2":
#     email = input ("Email > ")
#     if email in listOfEmail:
#       listOfEmail.remove(email)
#     prettyPrint()  
  
#   elif menu == "3":
#     prettyPrint()
    
#   time.sleep(1)
#   os.system("clear")
  
#-----------------------------------------------------------------------------------------------------

# otra forma de hacerlo es con el comando "Len"

# import os, time
# listOfEmail = []

# def prettyPrint():
#   os.system("clear") 
#   print("listofEmail") 
#   print()
#   for index in range(len(listOfEmail)): # len counts how many items in a list
#     print(f"{index}: {listOfEmail[index]}") 
#   time.sleep(1)

# while True:
#   print("SPAMMER Inc.")
#   menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
#   if menu == "1":
#     email = input("Email > ")
#     listOfEmail.append(email)
#   elif menu =="2":
#     email = input ("Email > ")
#     if email in listOfEmail:
#       listOfEmail.remove(email)
#   elif menu == "3":
#     prettyPrint() 
#   time.sleep(1)
#   os.system("clear")

#--------------------------------------- 1 example more -----------------------------------------------
# import os, time
# listOfFood = []

# def prettyPrint():
#   os.system("clear") 
#   print("listofFood") 
#   print()
#   counter = 1 
#   for order in listOfFood: 
#     print(f"{counter}.- {order}") 
#     counter += 1 
#   time.sleep(1)
# while True:
#   print("Yummy Food Restaurant")
#   menu = input("1. Order food\n2: Delete order\n3. Leave a review\n4. Delivery\n> ")
#   if menu == "1":
#     order = input("order > ")
#     listOfFood.append(order)
#   elif menu =="2":
#     order = input ("delete order> ")
#     if order in listOfFood:
#       listOfFood.remove(order)
#     else:
#       print(f"{order} was not in the list")
#   elif menu == "3": 
#     prettyPrint()
#   elif menu == "4":
#     print("Ok!, ur food was ordered, thanks")
#     break
#   else:
#     print("ERROR: pleaschoose a number between 1 and 4")
  
#   time.sleep(1)
#   os.system("clear")
 
  #-------------------------------------------------------------------------------------------------

# exercise:
import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear")
  print("listOfEmail")
  print()
  counter = 1
  
  for email in listOfEmail:
    print(f"{counter}: {email}")
    counter+=1
  time.sleep(1)

def spam(max):   
  for i in range(0,max):  # aqui meto el rango desde 0 al máximo que hayamos agregado en la lista
    print(f"""Email {i+1}   

Dear {listOfEmail[i]}
It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

Love and hugs,

Ian Spammington III""")     # el i+1 es porque yo ya soy el primero y el listOfEmail[i] nos va a spamer a cada correo añadido el mismo texto
    time.sleep(1)
    os.system("clear")
    
while True:
  print("SPAMMER Inc.")
  menu = input("1: Add email\n2: Remove email\n3: Show emails\n4: Get SPAMMING\n> ")
  
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
    
  elif menu== "2":
    email = input("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
      
  elif menu == "3":
    prettyPrint()
    
  elif menu =="4":
    spam(10)
    
  time.sleep(1)
  os.system("clear")