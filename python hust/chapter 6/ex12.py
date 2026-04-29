days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_averages = []

with open("files/steps.txt") as f:
    for days in days_in_month:
        total_steps = 0

        for _ in range(days):
            total_steps += int(f.readline())

        average = total_steps / days
        month_averages.append(average)

for i, avg in enumerate(month_averages):
    print(f"Month {i + 1}: {avg:.2f} step")
