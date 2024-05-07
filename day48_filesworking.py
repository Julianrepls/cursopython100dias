# f = open("savedFile.txt", "w")
# f.write("Hello there")
# f.close()


# f = open("savedFile2.txt", "a+") # al poner "a+" lo que hace es que cada vez que ejecute el programa va agregando lo que escribas
#                                  # para agregar solo una linea una sola vez ponemos "w" en lugar de "a+"
# wt = input("Write somthing> ")
# f.write(f"{wt}\n")
# f.close()


# ------------ CHALLENGE ------------

# Today's challenge is to create a high score table.

# Your program should:

# Ask the user to input their three letter initials and score (out of about 100,000).
# Save both those values into a file called 'high.score'.
# This should use append mode. If the file doesn't exist, it should be created. If it does, the score should be added to the end.
# Each new entry score should go on a new line as initials space score. Then start a new line for the next entry.
# Add 2-3 scores for testing in a loop.
# The loop should ask the user if they've finished entering data and stop if they have.

import os, time

while True:
  print("--- HIGH SCORE TABLE ---")
  print()

  name = input("INITIALS: ").upper()
  score = input("SCORE: ")
  print()

  f = open("day48.high.score", "a+")
  f.write(f"{name} {score}\n")
  f.close()

  print("ADDED")
  # time.sleep(2)
  # os.system("clear")
