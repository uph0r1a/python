print("Enter the total sales for the month: ", end="")
totalSale = float(input())

print(
    f"The amount of county sales tax: {totalSale * 0.025}\nThe amount of state sales tax: {totalSale * 0.05}\nThe total sales tax (county plus state): {totalSale + totalSale * (0.025 + 0.05)}"
)
