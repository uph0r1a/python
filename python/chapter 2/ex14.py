print("Enter the amount of principal originally deposited into the account: ", end="")
p = float(input())

print("Enter the annual interest rate paid by the account: ", end="")
r = float(input())

print("Enter the number of times per year that the interest is compounded: ", end="")
n = float(input())

print("Enter the number of years the account will be left to earn interest: ", end="")
t = float(input())

print(
    f"The amount of money in the account after the specified number of years: {round(p*((1+(r/100)/n)**n*t),2)}"
)
