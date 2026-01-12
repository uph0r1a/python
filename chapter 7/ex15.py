import matplotlib.pyplot as plt

gas_prices = []

with open("files/1994_Weekly_Gas_Averages.txt", "r") as file:
    for line in file:
        gas_prices.append(float(line.strip()))

weeks = list(range(1, len(gas_prices) + 1))

plt.figure(figsize=(10, 6))
plt.plot(weeks, gas_prices, marker="o", linestyle="-", color="blue")

plt.title("Average Weekly Gas Prices in 1994")
plt.xlabel("Week Number")
plt.ylabel("Average Gas Price (Dollars)")

plt.xticks(range(1, 53, 4))
plt.yticks([0.95, 1.00, 1.05, 1.10, 1.15, 1.20])

plt.grid(True)

plt.show()
