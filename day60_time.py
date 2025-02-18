import datetime

# myDate = datetime.date(year= 2022, month= 12, day= 16)
# print(myDate)

# today = datetime.date.today()
# print(today)

# day=int(input("Day: "))
# month=int(input("Month is: "))
# year=int(input("Year: "))

# date=datetime.date(year, month, day)
# print(date)

# today = datetime.date.today()
# holiday = datetime.date(year=2025, month=2, day=18)

# if holiday > today:
#     print("Coming soon")
# elif holiday < today:
#     print("hope u enjoyed it")
# else:
#     print("Happy holiday")

today = datetime.date.today()
holiday = datetime.timedelta(days=365)

newDate = today + holiday # podemos sumar fechas o sumar dias a una fecha como un int
print(newDate)