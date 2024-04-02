import random
# # myNumber =  random.randint(1,100)
# # print(myNumber)
# for i in range(10):
#     myNumber =  random.randint(1,100)
#     print(myNumber)

print("Welcome to Guess the Number.")
print()
print("Guess a number between 1 and 1,000,000 and I will tell you if you are right")
print()
print("Let's play!")

correct_number = random.randint(1,1000000)
print(correct_number)
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
    print("You took ", rounds, "rounds")
    break 
  else:
    print("That is not a number.")