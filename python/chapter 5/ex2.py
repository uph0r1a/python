def stateTax(amount):
    return amount * 0.05


def countyTax(amount):
    return amount * 0.025


def totalTax(amount):
    return round(stateTax(amount) + countyTax(amount), 2)


def total(amount):
    return amount + totalTax(amount)


print("Enter the amount of a purchase: ", end="")
amount = float(input())

print(
    f"Amount: {amount}\nState sales tax: {stateTax(amount)}\nCounty sale tax: {countyTax(amount)}\nTotal sales tax: {totalTax(amount)}\nTotal: {total(amount)}"
)
