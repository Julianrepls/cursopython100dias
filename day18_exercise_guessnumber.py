print("Welcome to Guess the Number.")
print()
print("Guess a number between 1 and 1,000,000 and I will tell you if you are right")
print()
print("Let's play!")

correct_number = 2300
rounds = 1

while True:
  user = int(input("Pick a number between 1 and 1,000,000: "))
  if user < 0:
    print("Now we'll never know what the answer is …")
    exit()
  if user < correct_number:
    print("That number is too low. Try again!")
    rounds += 1
  elif user > correct_number:
    print("That number is too high. Try again!")
    rounds += 1
    continue
  elif user == correct_number:
    print("You are a winner!")
    break 
  else:
    print("That is not a number.")