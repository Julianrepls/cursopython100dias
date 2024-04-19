dias_enaño = int(input("Ingrese el número de días del año: "))


dia_year = 365
dia_bisiesto = 366
hora_day = 24
min_hora = 60
sec_hora = 60

result = dia_year * hora_day * min_hora * sec_hora
dia_bisiesto = dia_bisiesto * hora_day * min_hora * sec_hora

if dias_enaño == 366:
  print("Número de segundos en un año bisiesto es: ", dia_bisiesto)
else:
  print("Número de segundos en un año es: ", result)


