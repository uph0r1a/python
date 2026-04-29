sales = []

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in days:
    amount = float(input(f"Enter sales for {day}: "))
    sales.append(amount)

total_sales = 0
for amount in sales:
    total_sales += amount

print(f"\nTotal sales for the week: ${total_sales:.2f}")
