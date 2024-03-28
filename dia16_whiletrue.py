# while True:
#   print("this is running")
#   goAgain = input("Go again?: ")
#   if goAgain == "no":
#     break
# print("I was in a toilette")

# print()
# counter = 0
# while True:
#   answer = int(input("Enter a number: "))
#   print("Adding a number")
#   counter += answer
#   print("Current total is", counter)
#   addOther = input("Add other number?: ")
#   if addOther == "no":
#     break
# print("Bye")

# while True:
#   color = input("Enter a color: ")
#   if color == "red":
#     break
#   else:
#     print("Cool color!")
# print("I don't like red")

counter = 1
print("Fill in the blank Lyrics")
print()
while True:

  lyric = input("Try, Never going to ______ you up:")
  
  if lyric.lower() == "put":
    print("correct, u got!")
  else:
    print("Nope, try again")
    counter += 1
  if lyric == "put":
    break
print("Thanks for playing")
print("You got the correct lyrics in", counter, "attempt(s).")
