f = open("day48.high.score", "r") #abrimos el documento y "r" para leerlo
contents = f.read() 
f.close()

contents = contents.split() #added split here

print(contents) #con esto estamos leyendo el contenido del documento day48.high.score

#----------------------- x -------------------------

f = open("filenames.list","r")
contents = f.readline().strip() # este comando .readline te lee una linea del documento pero lee solo una y para el programa, no lee el documento entero
print(contents)

#----------------------- x --------------------------
#para leer linea a linea del documento hasta que se encuentre un espacio en blanco deberíamos hacer esto:

f = open("day48.high.score", "r")

while True:
    contents = f.readline().strip() #lee linea a linea y salta a la siguiente el documento en bucle
    if contents =="":
        break # el bucle se para cuando ve un espacio en blanco

    print(contents)
f.close()
 
# ---------------  CHALLENGE ----------------

# Your program should:

# 1. Read in the data from the high.score file.
# 2. Identify which of those users had the highest score. Automatically! (Not you doing it!)
# 3. Output the name and score of the winner.

"""
EN EL DAY48 CREÁBAMOS UN DOCUMENTO Y METIAMOS UN NOMBRE CON UNA PUNTUACION Y AHORA VAMOS A TRABAJAR CON ESE DOCUMENTO
EN ESTE EJERCICIO VAMOS A PEDIR QUE NOS DEVUELVA LA PUNTUACION MAS ALTA EN ESE DOCUMENTO (day48.high.score)
"""

f = open("day48.high.score", "r")
score = f.read().split("\n")
f.close()

highScore = 0
name = None

for rows in score:
    data = rows.split()
    print(data) #leyendo los valores y separandolos en una lista con dos elementos
    if data != []:
        if int(data[1]) > highScore:
            highScore = int(data[1])
            name = data[0]

print("The winner is", name, "with", highScore)


