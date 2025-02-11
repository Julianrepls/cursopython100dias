import csv

total = 0.0

with open("cuentas.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total += float(row["Unidades"]) * float(row["Precio"])

print(f"Total: ${round(total, 2)}")

# total = 0.0
# Esto nos lee el documento CSV, to read the CSV file:
# with open("cuentas.csv") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(", ".join(row))

# total = 0.0
# with open("cuentas.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row["Total"])
#         total += float(row["Total"])
# print(f"Total: {total}")