# total = 0
# for number in range (10):
#   total += number
#   print(total)

# days = 0
# for days in range (7):
#   print("Day", days+1)

loan = 1000
int = 0.05
for i in range(10):
  loan +=(loan*int)
  print("Year", i+1, "is", round(loan,2))
