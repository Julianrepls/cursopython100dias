class animal:
    species: None
    name: None
    sound: None
    # estas con las cosas que vamos a almacenar dentro de la clase animal

    def __init__(self, name, species, sound): #el self, funciona como un enlace

        self.name = name
        self.species = species
        self.sound = sound
        #asi es como se crea una plantilla para un animal

    def talk(self):
        print(f"{self.name} says {self.sound}")

#ahora vamos a crear una nueva clase

class bird(animal):
    
    color = None

    def __init__(self, color):
        self.name = "Bird"
        self.species = "Avian"
        self.sound = "Tweet"
        self.color = color
    # crear esta nueva clase (pájaro) nos permite heredar del perro el name, specie, sound 
    #   al llamar el "class (animal)" al poner animal ente parentesis heredamos todos los atribunos de animal
    #       incluso podemos agregarle otro atributo como el color



dog = animal("Dog", "canine", "Woof")
print(dog.name)
print(dog.talk)
print()

cow = animal("Cow", "Bo Taurus", "Muu") # así es como puedo crear un nuevo animal con la plantilla 
print(cow.sound) # de esta forma es como llamo al sonido que hace la vaca
print(cow.talk)
print()

polly = bird("Green") # aqui llamamos a nuestro pájaro Polly y le damos un color como bien hemos definido arriba el Color
polly.talk()
print(polly.color)
