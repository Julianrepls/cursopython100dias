bill = float(input("¿cuanto es la multa?: "))
print()
personas = int(input("¿cuantas personas pagaraán la multa? "))
print()
propina = float(input("¿cuanto de propina van a dejar por persona? "))
print("------------------------")
total = bill / personas
total = round(total, 2)
print("el total a pagar por persona es de ", total)
print()
total_propina = propina * personas
total_propina = round(total_propina, 2)
print("El total de la propina es: ", total_propina)
total_todo = total + propina
print()
print("el total a pagar por persona, inculuido propina es de: ", total_todo)