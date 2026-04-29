print("Enter the loan payment: ", end="")
loanPayment = float(input())

print("Enter the insurerance: ", end="")
insurance = float(input())

print("Enter the gas: ", end="")
gas = float(input())

print("Enter the oil: ", end="")
oil = float(input())

print("Enter the tires: ", end="")
tires = float(input())

print("Enter the maintenance: ", end="")
maintenance = float(input())

print(
    f"Monthly cost: {loanPayment + insurance + gas + oil + tires + maintenance}\nAnnual cost: {(loanPayment + insurance + gas + oil + tires + maintenance) * 12}"
)
