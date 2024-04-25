my2DList = [ ["Johnny", 21, "Mac"],
 ["Sian", 19, "PC"],
 ["Gethin", 17, "PC"] ]

print(my2DList[0][1]) # this code outputs: 21


# #// other way:
my2DList = [ ["Johnny", 21, "Mac"], ["Sian", 19, "PC"], ["Gethin", 17, "PC"] ]

print(my2DList[0]) # This code outputs ['Johnny', 21, 'Mac'].
print(my2DList[0][0]) #this code otputs: 'Johnny'

my2DList = [ ["Johnny", 21, "Mac"],
   ["Sian", 19, "PC"],
   ["Gethin", 17, "PC"] ]

print(my2DList[0][0])
# This code outputs 'Johnny'. It's Johnny's name from list 0 (first square bracket), item 0 (second square bracket)

print(my2DList[1][2])
# This code outputs 'PC'. It's Sian's computing preferene from list 1 (first square bracket), item 2 (second square bracket)

#//// Editing a 2D list:
my2DList = [ ["Johnny", 21, "Mac"],
   ["Sian", 19, "PC"],
   ["Gethin", 17, "PC"] ]

my2DList[1][2] = "Linux" 
# The line above changes list 1, item 2 from PC to Linux

print(my2DList[1]) # this outputs: Linux
# I'm using this line to output list 1 to check that the change has happened correctly.

#----------------- challange ---------------- 
# Today's challenge is to create a bingo card. Oh yes, because programming's not just for you hip, young cats. 😆

# Anyway, your challenge is to enable "gambling for the elderly" (aka Bingo), and you'll achieve it like this:

# Randomly generate a series of number between 0 and 90.
# Allocate each number to a place in a 2D list.
# The numbers should be in numerical order, left to right.
# Numbers should not be repeated.
# The center square should not contain a number. It should contain the word 'BINGO!'.
# When the program is run, the bingo card should be displayed on screen.


import random

bingo = []

def ran():
  number = random.randint(1,90)
  return number

def prettyPrint():
  for row in bingo:
    print(row)

numbers = []
for i in range(8):
  numbers.append(ran())

numbers.sort()

bingo = [ [ numbers[0], numbers[1], numbers[2]],
          [ numbers[3], "BINGO", numbers[4] ],
          [ numbers [5], numbers[6], numbers[7]]
        ]

prettyPrint()