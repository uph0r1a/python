import matplotlib.pyplot as plt

categories = []
amounts = []

with open("files/expenses.txt", "r") as file:
    for line in file:
        category, amount = line.strip().split(",")
        categories.append(category)
        amounts.append(float(amount))

plt.figure(figsize=(8, 8))
plt.pie(amounts, labels=categories, autopct="%1.1f%%", startangle=140)
plt.title("Monthly Expenses Breakdown")
plt.axis("equal")

plt.show()
