# --------------- EXCERCISE  ---------------
"""
Vamos a crear como un diario en el que vamos a escribir nuestras ideas
Que nos permita agregar nuestras ideas y que sean guardadas en un archivo de texto y que también se pueda leer, elegir una al azar y mostrar la lista de ideas.
"""
# 1. Prompt the user to add an idea, or load a random one.
# 2. Choosing 'Add an idea' results in:
#   - A prompt for the user to input their idea.
#   - Add the idea to a text file called 'my.ideas'.
#   - Add the idea in append mode, with every new idea on a brand new line.
# 3. Choosing 'Load random' results in:
#   - Load the list of ideas.
#   - Choose one at random.
#   - Display it on screen for a few seconds.
#   - Return to the menu.




import os, time, random 

def add():
    os.system("clear")
    idea = input("idea: ")
    f = open("day50.my.ideas", "a+")
    f.write(f"{idea}\n")
    f.close()

def show():
    f = open("day50.my.ideas", "r")
    ideas = f.read().split("\n")
    f.close()
    ideas.remove("")
    idea = random.choice(ideas)
    print(f"The random is> {idea}")
    print()

    
    
while True:
    menu = input("1: Add idea\n2: Show random idea\nChose 1 or 2: ")
    if menu == "1":
        add()
        print("...Idea ADDED")
        
    else:
        print()
        show()
        