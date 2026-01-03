import calendar

month = day = year = 0

print("Enter month: ", end="")

while 1:
    month = int(input())
    if month >= 1 and month <= 12:
        break
    print("Invalid month\nRe-enter month: ", end="")

print("Enter year: ", end="")

while 1:
    year = int(input())
    if year >= 0:
        break
    print("Invalid year\nRe-enter year: ", end="")

print("Enter day: ", end="")
while 1:
    day = int(input())
    if day >= 1 and day <= calendar.monthrange(year, month)[1]:
        break
    print("Invalid day\nRe-enter day: ", end="")

if day * month == year % 100:
    print("The date is magic")
else:
    print("The date is not magic")
