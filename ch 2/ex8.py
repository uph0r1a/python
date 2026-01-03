print("Enter the charge for the food: ", end="")
amountOfMeal = float(input())

print(
    f"Charge for food: {amountOfMeal}\nTip: {amountOfMeal*0.18}\nSales tax: {amountOfMeal*0.07}\nTotal: {amountOfMeal*(1+0.18+0.07)}"
)
