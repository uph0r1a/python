rainfall = []

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

for month in months:
    amount = float(input(f"Enter rainfall for {month}: "))
    rainfall.append(amount)

total_rainfall = sum(rainfall)
average_rainfall = total_rainfall / 12

highest = max(rainfall)
lowest = min(rainfall)

highest_month = months[rainfall.index(highest)]
lowest_month = months[rainfall.index(lowest)]

print(
    f"\nTotal rainfall for the year: {total_rainfall}\n"
    f"Average monthly rainfall: {average_rainfall}\n"
    f"Highest rainfall: {highest} in {highest_month}\n"
    f"Lowest rainfall: {lowest} in {lowest_month}"
)
