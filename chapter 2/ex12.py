numberOfSharesPurchased = 2000
stockPerSharePurchased = 40
commissionPurchased = 0.03
numberOfSharesSold = 2000
stockPerShareSold = 42.75
commissionSold = 0.03

moneyPaidForStock = numberOfSharesPurchased * stockPerSharePurchased
commissionPaidOnPurchase = moneyPaidForStock * commissionPurchased
moneySoldForStock = numberOfSharesSold * stockPerShareSold
commissionPaidOnSale = moneySoldForStock * commissionSold

netAmount = (
    moneySoldForStock
    - commissionPaidOnSale
    - moneyPaidForStock
    - commissionPaidOnPurchase
)

print(
    f"The amount of money Joe paid for the stock: {moneyPaidForStock}\n"
    f"The amount of commission Joe paid his broker when he bought the stock: {commissionPaidOnPurchase}\n"
    f"The amount for which Joe sold the stock: {moneySoldForStock}\n"
    f"The amount of commission Joe paid his broker when he sold the stock: {commissionPaidOnSale}\n"
    f"The amount of money that Joe had left: {netAmount}\n"
    f"{'Profit' if netAmount > 0 else 'Loss'}"
)
