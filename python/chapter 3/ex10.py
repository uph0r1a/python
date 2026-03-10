print("Enter the number of pennies: ", end="")
pennies = float(input())

print("Enter the number of nickels: ", end="")
nickels = float(input())

print("Enter the number of dimes: ", end="")
dimes = float(input())

print("Enter the number of quarters: ", end="")
quarters = float(input())

dollar = pennies * 0.01 + nickels * 0.05 + dimes * 0.1 + quarters * 0.25

print(
    "You win"
    if dollar == 1
    else (
        f"{round(dollar - 1)} more than 1 dollar"
        if dollar > 1
        else f"{round(1 - dollar)} less than 1 dollar"
    )
)
