def main():
    prices = []

    with open("GasPrices.txt", "r") as file:
        for line in file:
            date, price = line.strip().split(":")
            month, day, year = date.split("-")
            prices.append((date, int(month), int(year), float(price)))

    year_prices = {}
    month_prices = {}
    year_high_low = {}

    for date, month, year, price in prices:
        year_prices.setdefault(year, []).append(price)

        month_prices.setdefault(month, []).append(price)

        if year not in year_high_low:
            year_high_low[year] = {"high": (date, price), "low": (date, price)}
        else:
            if price > year_high_low[year]["high"][1]:
                year_high_low[year]["high"] = (date, price)
            if price < year_high_low[year]["low"][1]:
                year_high_low[year]["low"] = (date, price)

    print("Average Price Per Year:")
    for year in sorted(year_prices):
        avg = sum(year_prices[year]) / len(year_prices[year])
        print(year, f"${avg:.2f}")

    print("\nAverage Price Per Month:")
    for month in sorted(month_prices):
        avg = sum(month_prices[month]) / len(month_prices[month])
        print(month, f"${avg:.2f}")

    print("\nHighest and Lowest Prices Per Year:")
    for year in sorted(year_high_low):
        high = year_high_low[year]["high"]
        low = year_high_low[year]["low"]
        print(year)
        print("  High:", high[0], f"${high[1]:.2f}")
        print("  Low :", low[0], f"${low[1]:.2f}")

    prices_sorted_low = sorted(prices, key=lambda x: x[3])
    prices_sorted_high = sorted(prices, key=lambda x: x[3], reverse=True)

    with open("files/prices_low_to_high.txt", "w") as file:
        for p in prices_sorted_low:
            file.write(f"{p[0]} ${p[3]:.2f}\n")

    with open("files/prices_high_to_low.txt", "w") as file:
        for p in prices_sorted_high:
            file.write(f"{p[0]} ${p[3]:.2f}\n")

    print("\nPrice lists written to files.")


if __name__ == "__main__":
    main()
