import random, os, time

totalAttemps = 0

def game():
    attemps = 0
    number = random.randint(1,100)
    while True:
        
        guess = int(input("pick a number between 1 and 100: "))
        if guess > number:
            print("Too high")
            attemps += 1
        
        elif guess < number:
            print(" too low ")
            attemps +=1

        else:
            print("just right")
            print(f"{attemps} attempets this round")
            return attemps
while True:
    menu = int(input("1: Guess the random number game\n2: Total Score\n3: Exit\n> "))
    if menu == 1:
        totalAttemps += game()
    elif menu == 2:
        print(f"You ve had {totalAttemps} attemps")
    else:
        break