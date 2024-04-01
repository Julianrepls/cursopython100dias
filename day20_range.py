# for i in range(100,110):
#     print(i+1)
# print()
# print("Thirteen table")
# for i in range(1,13):
#     print(i, "x 13 =", i*13)
# print()
for i in range(0, 500, 25):
    print(i)   #cuando ponemos 3 valores, el primero sera el inicial (0), el segundo será el límite (500) y el tercero será el incremento por cada vuelta.
print()
# for i in range(10, 0, -1):
#     print(i)
print()
for i in range(20,40,1):
  print(i)

print()
print("Welcome to to my number list generator....")
u = int(input("Enter a number to start with: "))
v = int(input("Enter a number to end with: "))
w = int(input("Enter a number to count by: "))

for i in range(u,v,w):
  print(i)