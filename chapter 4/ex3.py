print("Enter your budget: ", end="")
budget = float(input())
choice = ""
sum = 0

while choice.lower() != "no":
    print("Enter the expenses: ", end="")
    sum += float(input())
    print("Do you want to continue: ", end="")
    choice = input()

print(f"Overbudget: {sum - budget}" if sum > budget else f"Underbudget: {budget - sum}")
