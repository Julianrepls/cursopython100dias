#Challenge: countdown timer. Automatically work out today's date and then ask user the name of event as well as the day, month, year its going to be happening
#work our the amount of days until that even happens display it on the screen; if the even is happening today insert happy face; if the date in the past insert sad face.


# vamos a calcular autmaticamente la fecha de hoy y luego le vamos a pedir al usuario la fecha de un evento
# luego calcularemos los días que faltan hasta el evento o en caso contrario, cuanto tiempo hace que sucedió; y lo mostramos en pantalla

import datetime

today = datetime.date.today()

print(" == COUNTDOWN TIMER == ")
day = int(input("What Day: "))
month = int(input("What Month: "))
year = int(input("Inser the Year: "))
event = datetime.date(year, month, day)

difference = event - today
difference = difference.days # esta es la clave: lo que hace es que extrae la cantidad de dias de diferencia del tiempo Delta y eso nos permite tratarle como un numero entero

if difference > 0:
    print(difference)
elif difference < 0:
    print("T_T")
else:
    print("=)")