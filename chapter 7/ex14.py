import matplotlib.pyplot as plt

categories = []
amounts = []

try:
    with open("files\expenses.txt") as file:
        for line in file:
            category, amount = line.strip().split(",")
            categories.append(category)
            amounts.append(float(amount))

except Exception as e:
    print(f"Error: {e}")
    exit()

if categories and amounts:
    plt.figure(figsize=(8, 8))
    plt.pie(amounts, labels=categories, autopct="%1.1f%%", startangle=140)
    plt.title("Monthly Expenses Breakdown")
    plt.axis("equal")
    plt.show()
else:
    print("No valid expense data to display.")
