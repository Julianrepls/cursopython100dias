# in a CSV file that contains a list of music. We going to search through that list and categorize them by artist
# creating a folder for each of the artists using the OS library put in one blank text file for each of the songs with the file name as the name of the song
# should end up with multiple folders each of the artist and multiple individual text files withhin that folder for each of the songs and might be thinking why might
# we just dont have the copyright to be able to do that in a replicas unfortunately 

# en un archivo CSV que contiene una lista de musica. Vamos a buscar en esa lista y categorizarlas por atistas
# lo vamos a hacer de forma que creamos una carpeta para cada uno de los artistas usando la librería de OS
# vamos a poner un archivo de texto en blanco para cada una de las canciones con el nombre del archivo como el nombre de la canción
# deberíamos acabar con múltiples carpetas y múltiples archivos de texto individuales dentro de esa carpeta para cada una de las canciones  

import csv, os

with open("musiclist.csv") as file: 
    reader = csv.DictReader(file)
    for row in reader:
       dir = os.listdir()
       artist = row["artist"].title()
       print(artist)
       if artist not in dir:
           os.mkdir(artist)
       song = row["song"]
       print(row["song"])
       path= os.path.join(f"{artist}/", song)
       f = open(path, "w")
       f.close()


