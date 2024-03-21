# age = input("Ingrese su edad: ")
# if age > 18:
#     print("Usted es mayor de edad")
# else:
#     print("Usted es menor de edad")

print("--------- GENERACIONES ---------")
year = int(input("Ingrese su año de nacimiento: "))
if year <= 1846:
    print("No se puede determinar su generacion")
elif year >= 1883 and year <= 1900:
    print("Su generacion es: Lost Generation")
elif year >= 1901 and year <= 1927:
    print("Su generacion es: Greatest Generation")
elif year >= 1928 and year <= 1945:
    print("Su generacion es: Silent Generation")
elif year >= 1946 and year <= 1964:
    print("Su generacion es: Baby Boomers")
elif year >= 1965 and year <= 1980:
    print("Su generacion es: Generation X")
elif year >= 1981 and year <= 1996:
    print("Su generacion es: Millennials")
elif year >= 1997 and year <= 2012:
    print("Su generacion es: Generation Z")
else:
    print("Su generacion es: Generation Alpha")

print("Veamos si conoces el valor del número pi")
pinum = float(input("Ingrese un numero: "))
if pinum == 3.14:
  print("correcto")
else:
  print("no es correcto")
