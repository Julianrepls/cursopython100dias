print("Bienvenido a tu diario")
name = input("¿Cómo te llamas? ")

if name == "Juan" or name == "juan":
  day = input("Que dia de la semana es hoy?: ")
  if day== "lunes" or day== "Lunes":
    print("Es el peor día de la semana pero no worries", name)
  if day == "martes" or day == "Martes":
    print("vamos un día menos de jornada semanal")
  if day == "miercoles" or day == "Miercoles":
    print("estamos en el ecuador de la semana ánimo", name)
  if day == "jueves" or day == "Jueves":
    print("ya casi es viernes", name)
  if day == "viernes" or day == "Viernes":
    print(name, "puedes tomarte un respiro!")
elif name == "Maria" or name == "maria":
  mes = input("¿En que mes estamos? ")
  if mes == "enero" or mes == "Enero":
    print("vas a teneres que llevar una abrigo si vas a la calle")
  if mes == "mayo" or mes == "Mayo":
    print("ya casi es el mes de la madre")
  if mes == "abril" or mes == "Abril":
    print(name, "no olvides llevar parguas!")
  if mes == "junio" or mes == "Junio":
    print("ya va pegando playa", name)
else:
  print("no te conozco, pero bienvenido")
