debugMode= False

myList = []

try:
    f = open("List.mine", "r")
    myList = eval(f.read())
    f.close()

# except Exception as err:
#     print("Error: unable to load")
#     print(err)
# Esto lo que hace es que que nos dice que hay un error de manera muy generalizada pero no tan específico

except:
    print("ERROR")
    if debugMode:
        print(traceback) # con esto nos dan un seguimiento de donde está el error paso a paso.

for row in myList:
    print(row)
