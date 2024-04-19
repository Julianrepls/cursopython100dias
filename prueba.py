import time
print()
print("--- Bienvenido al creador de Usuario ---")
print()
user = input("introduce tu user> " )
time.sleep(1)
pw = input("introduce tu pw> ")
time.sleep(1)
print()

enter = "yes"
while enter == "yes":
    

    print("Muy buenas", user)
    pw2 = input("Introduce tu pasword para entrar: \n")
    time.sleep(1)
    
    if pw == pw2:
        print("bienvenido", user,"!!")
        break
    
    else:
        print()
        pw = input("La contraseña es incorrecta, intente de nuevo>  ")
        while pw != pw2:
            if pw == pw2:
                print("bienve")
                break
            else: 
                continue

    enter = input("Desea entrar en la página?> \n")
    if enter == "no":
        break
    else: 
        continue

