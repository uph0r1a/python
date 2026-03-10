print("Enter the amount of a purchase: ", end="")
amount = float(input())

print(
    f"Amount: {amount}\nState sales tax: {amount * 0.05}\nCounty sale tax: {amount * 0.025}\nTotal sales tax: {round(amount * (0.05 + 0.025),2)}\nTotal: {amount*(1 + 0.05 + 0.025)}"
)
