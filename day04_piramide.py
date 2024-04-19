print("== Esta es una pequeña historia egipcia ==")
print("Esta historia te sumergerá en el antiguo Egipto donde tu serás el elegido sobre el futuro de la humanidad")
print("Si no te atreves a entrar en la pirámide escribe: Salir, a la hora de elegir la pirámide")
print()
name = input("Tu nombre es: ")
# enemy = input("Tu enemigo es: Set, Ra, Anubis")


god = ""

while True:
    if not god:
        god = input("Elije en que pirámide entrar Set, Ra, Anubis:  ")
        if god.lower() == "salir":
            print("El terror te impidió entar en la pirámide")
            break

        if god.lower() == "Set":
            print("Cuando\033[36m", name,
            "\033[0mirrumpió en la cámara funeraria donde descansaba la momia \033[35mSet\033[0m, vitoreó muy alegremente porque finalmente había logrado desmantelar todas las trampas mortales que la pirámide ocultaba. Sin embargo, poco sospechaba que quien más se alegraba de su logro era la momia \033[35mSet\033[0m, ya que las trampas de la pirámide no eran para prevenir que los asalta tumbas entraran a llevarse sus tesoros, si no para impedir que ella saliera, así que ahora podría escapar fácilmente a \033[35m'dejar calva' \033[0ma toda la Humanidad.")
            break
        god = str(god)
        
        if god == "Ra":
            print("Cuando\033[36m", name,
            "\033[0mirrumpió en la cámara funeraria donde descansaba la momia \033[35mRa\033[0m, vitoreó muy alegremente porque finalmente había logrado desmantelar todas las trampas mortales que la pirámide ocultaba. Sin embargo, poco sospechaba que quien más se alegraba de su logro era la momia \033[35mRa\033[0m, ya que las trampas de la pirámide no eran para prevenir que los asalta tumbas entraran a llevarse sus tesoros, si no para impedir que ella saliera, así que ahora podría escapar fácilmente a \033[35menviar una plaga\033[0m a  toda la Humanidad.")
            break
        god = str(god)
        
        if god == "Anubis":
            print("Cuando\033[36m", name,
            "\033[0mirrumpió en la cámara funeraria donde descansaba la momia \033[35mAnubis\033[0m, vitoreó muy alegremente porque finalmente había logrado desmantelar todas las trampas mortales que la pirámide ocultaba. Sin embargo, poco sospechaba que quien más se alegraba de su logro era la momia \033[35mAnubis\033[0m, ya que las trampas de la pirámide no eran para prevenir que los asalta tumbas entraran a llevarse sus tesoros, si no para impedir que ella saliera, así que ahora podría escapar fácilmente para \033[35m destruir\033[0m toda la Humanidad..")
            break
    else:
        print("No has seleccionado En que pirámide entrar")
        break

