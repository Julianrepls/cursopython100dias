import os

# files = os.listdir()
# if "quickSave.txt" not in files:
#     print("Error: not found")

#os.mkdir("bye") # si ejecutamos esto lo que hace es crear una carpeta con ese nombre entre comillas

#os.rename("myName.txt", "New.o") # esto hace que cambie de nombre un archivo ya existente, en este caso cambia myName de nombre por "New.o" de manera inmediata


# f = open("bye/aFile.txt", "w") # de esta manera lo que estamos haciendo es crear el archivo "aFile.txt" dentro de la carpeta bye
# f.write("hi")
# f.close()

# ahora vamos a hacer lo mismo que lo que acabamos de hacer pero de un método diferente y más fiable:

filename = os.path.join("bye/", "bFile.txt")

f = open(filename, "w")
f.write("hi")
f.close()
