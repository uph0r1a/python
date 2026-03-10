def main():
    prices = []

    try:
        with open("files/GasPrices.txt") as file:
            for line in file:
                date, price = line.strip().split(":")
                month, day, year = date.split("-")
                prices.append((date, int(month), int(year), float(price)))

    except Exception as e:
        print(f"Error: {e}")
        return

    year_prices = {}
    month_prices = {}
    year_high_low = {}

    # Process data
    for date, month, year, price in prices:
        if year in year_prices:
            year_prices[year].append(price)
        else:
            year_prices[year] = [price]

        if month in month_prices:
            month_prices[month].append(price)
        else:
            month_prices[month] = [price]

        if year not in year_high_low:
            year_high_low[year] = {
                "high_date": date,
                "high_price": price,
                "low_date": date,
                "low_price": price,
            }
        else:
            if price > year_high_low[year]["high_price"]:
                year_high_low[year]["high_price"] = price
                year_high_low[year]["high_date"] = date

            if price < year_high_low[year]["low_price"]:
                year_high_low[year]["low_price"] = price
                year_high_low[year]["low_date"] = date

    print("Average Price Per Year:")
    for year in year_prices:
        total = 0
        for p in year_prices[year]:
            total += p
        avg = total / len(year_prices[year])
        print(year, f"${avg:.2f}")

    print("\nAverage Price Per Month:")
    for month in month_prices:
        total = 0
        for p in month_prices[month]:
            total += p
        avg = total / len(month_prices[month])
        print(month, f"${avg:.2f}")

    print("\nHighest and Lowest Prices Per Year:")
    for year in year_high_low:
        print(year)
        print(
            "  High:",
            year_high_low[year]["high_date"],
            f"${year_high_low[year]['high_price']:.2f}",
        )
        print(
            "  Low :",
            year_high_low[year]["low_date"],
            f"${year_high_low[year]['low_price']:.2f}",
        )

    prices_low_to_high = prices[:]
    for i in range(len(prices_low_to_high)):
        for j in range(i + 1, len(prices_low_to_high)):
            if prices_low_to_high[i][3] > prices_low_to_high[j][3]:
                prices_low_to_high[i], prices_low_to_high[j] = (
                    prices_low_to_high[j],
                    prices_low_to_high[i],
                )

    with open("files/prices_low_to_high.txt", "w") as file:
        for date, month, year, price in prices_low_to_high:
            file.write(f"{date} ${price:.2f}\n")

    with open("files/prices_high_to_low.txt", "w") as file:
        for i in range(len(prices_low_to_high) - 1, -1, -1):
            date, month, year, price = prices_low_to_high[i]
            file.write(f"{date} ${price:.2f}\n")

    print("\nPrice lists written to files.")


main()
