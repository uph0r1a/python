print("Enter the starting number of organisms: ", end="")
startNumber = float(input())

print("Enter the average daily population increase (as a percentage): ", end="")
populationIncrease = float(input())

print("Enter the number of days the organisms will be left to multiply: ", end="")
numberOfDay = int(input())

print(f"{"Day Approximate":<10}{"Population"}\n--------------------")

for i in range(1, 11):
    print(f"{i:<10}{round(startNumber,3)}")
    startNumber += startNumber * (populationIncrease / 100)
