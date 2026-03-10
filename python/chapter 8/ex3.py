months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

date = input("Enter a date: ")
day = month = year = ""
count = 0

for i in range(len(date)):
    if date[i] == "/":
        count += 1
        continue

    if count == 0:
        month += date[i]

    if count == 1:
        day += date[i]

    if count == 2:
        year += date[i]

print(months[int(month) - 1] + " " + day + ", " + year)
