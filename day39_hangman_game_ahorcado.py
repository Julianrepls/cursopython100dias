import random

list =["capibara", "lemur", "galago", "comadreja", "tejon"]

letterpicked = []

word = random.choice(list)
lives = 5

while True:
    letter = input("di una letra: ")
    if letter in letterpicked:
        print("esa letra ya la has elegido")
        continue
    letterpicked.append(letter)
    if letter in word:
        print("you found a letter")
    else:
        print("No, not in there")
        lives -=1
        
    
    allLetters = True
    print()
    for i in word:
        if i in letterpicked:
            print(i, end="")
        else:
            print("_", end="")
            allLetters = False
    print()

    if allLetters:
        print(f"You won with {lives}")
        break
        
    if lives <=0:
        print(f"te fuiste, the answer was {word}")
        break
    else:
        print(f"only have {lives}")

