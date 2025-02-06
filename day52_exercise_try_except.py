import os, time
rolling = []

try:
    f = open("rolling.txt", "r")
    rolling = eval(f.read())
    f.close()

except:
 print("No existing Pizza list")

def viewRolling():
    h1 = "Name"
    h2 = "Topping"
    h3 = "Size"
    h4 = "Quantity"
    h5 = "Total"
    print(f"{h1:^10}{h2:^20}{h3:^10}{h4:^10}{h5:^10}")
    for row in rolling:
       print(f"{row[0]:^10}{row[1]:^10}{row[2]:^10}{row[3]:^10}{row[4]:^10}")
    #time.sleep(2)

def addRolling():
   time.sleep(1)
   os.system("clear")
   name = input("Name> ")
   topping = input("Toppings> ")
   size = input("Size (n/m)> ").lower()
   while True:
       try:
           qty=int(input("Quanty: "))
           break
       except:
           print("ERROR")
   cost=0
   if size =="s":
       cost=4.99
   else:
       cost=6.99
   total = cost * qty
   total = round(total, 2) #recuerda, esto es para redondear a 2 decimales
   row = [name, topping, size, qty, total]
   rolling.append(row)
    
#    while True:
#       try: #esto hace que si no escrbribes la cantidad correcta (un numero entero) se rompe la cadena y vuelve a intentar
#             qty = int(input("Quantity>  "))
#             break #si escribes correctamente la cantidad te saca del bucle
#       except:
#             print("ERROR: Quantity has to be int number")
#     cost = 0
#    if size == "s":
#         cost = 4.99
#     else:
#         cost = 6.99
#     total = cost * qty
#     total = round(total, 2) #recuerda, esto es para redondear a 2 decimales
#     row = [name, topping, size, qty, total]
#     rolling.append(row)
   


while True:
   time.sleep(1)
   os.system("clear")
   print(" - Sweet Rolling -")
   print()
   menu = input("1: Add Rolling\n2: View Rolling\n> ")
   if menu == "1":
      addRolling()
   else:
      viewRolling()
      f = open("rolling.txt", "w")
      f.write(str(rolling))
      f.close()
    



