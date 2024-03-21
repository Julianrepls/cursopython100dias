print("------------ VEAMOS CUANTO SABES SOBRE HARRY POTTER O STAR WARS--------------")
pelicula = input("¿Cuál es tu película favorita?")
if pelicula == "Harry Potter":
    print("Veamos cuanto sabes sobre sus personajes...")
    print()
    person = input(
        "Que personaje vamos a cuestionar? Harry Potter, Hermione o Ron?")
    if person == "Harry Potter":
        print("hmm... ")
        print()
        brother = input("sus hermanos son Ron y Hermione?")
        if brother == "si":
            print("Ajá! no sabes nada, no es tu peli favorita")
        else:
            print("¡Correcto! Seguramente es tu peli favorita")
    elif person == "Hermione":
        print("hmm... ")
        print()
        spell = input("Cual es el mejor hechizo de Hermione?")
        if spell == "Wingardiu Leviousa":
            print("¡Correcto! Seguramente es tu peli favorita")
        else:
            print("Ajá has fallado! no creo que sepas mucho sobre la película")
    elif person == "Ron":
        print("hmm... veamos cuanto sabes de Ron")
        print()
        pet = input("¿cual es la mascota de Ron?")
        if pet == "rata":
            print("¡Correcto! Seguramente es tu peli favorita")
        else:
            print("Ajá has fallado! no creo que sepas mucho sobre la película")
    else:
        print(
            "No has elegido uno de los personajes, Harry Potter, Hermione o Ron"
        )
elif pelicula == "Star Wars":
    print("Buena elecciñon, veamos que sabes sobre sus personajes...")
    print()
    person = input("Que personaje vamos a cuestionar: Luke o Han?")
    if person == "Luke":
        print()
        jedi = input("¿Es un Jedi o un Sith? ")
        if jedi == "Jedi":
            print("Claro que sí, es un Jedi, puede que sea tu peli favorita ")
        else:
            print("Es un Jedi por dios!, no tienes ni idea de Star Wars!...")
    elif person == "Han":
        print()
        nave = input("Cuál es su nave? Alcon milenario o Estrella Muerte?")
        if nave == "Alcon milenario":
            print("¡Correcto! Seguramente es tu peli favorita")
        else:
            print("Se nota que no tienes ni idea :(")
else:
    print("No has elegido una de las dos películas")
