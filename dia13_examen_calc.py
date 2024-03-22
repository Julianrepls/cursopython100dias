print("Exam calcuator")
print()
print("Max scrore: 100")
name_exam = input("Name of exam: ")
total_score = int(input("MX scroe: "))
score = int(input("Your scroe: "))
print()


number_score = float(score / total_score)
final_number = round(number_score, 2)
porcentaje = round(float(score / total_score)*100, 2)

print("You got",porcentaje,"%")


if final_number <= .49:
  print("You got U")
elif final_number >= .50 and final_number < .59:
  print("You got D")
elif final_number >= .60 and final_number < .69:
  print("You got C")
elif final_number >= .70 and final_number < .79:
  print("You got B")
elif final_number >= .80 and final_number < .89:
  print("You got A-")
elif score >= .90:
  print("You got A+")
else:
  print("Max is 100")
