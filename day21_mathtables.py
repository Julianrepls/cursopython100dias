print("Welcom to my math game")
print()
counter = 0

number = int(input("DName your multiples: "))
for i in range(1, 11):
    correct = i*number
    print(i, "x", number)
    answer = int(input("> "))
    if answer == correct:
        print("It's correct")
        counter +=1
    else:
        print("That's no correct, the correct is", correct)
        
if counter == 10:
    print("WoW perfect!")
else:
    print("has conseguido", counter)

