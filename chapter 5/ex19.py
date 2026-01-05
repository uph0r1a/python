def f(p, i, t):
    return p * ((1 + i) ** t)


print("Enter the account's present value: ", end="")
p = float(input())

print("Enter the monthly interest rate: ", end="")
i = float(input())

print("Enter the number of months that the money will be left in the account: ", end="")
t = float(input())

print(f"The future value of the account after the specified time period: {f(p,i,t)}")
