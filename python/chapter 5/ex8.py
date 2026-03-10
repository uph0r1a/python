print("Enter the square feet of wall space to be painted: ", end="")
wallSpace = float(input())

print("Enter the price of paint per gallon: ", end="")
paintPrice = float(input())

print(
    f"The number of gallons of paint required: {wallSpace / 112 * 1}\nThe hours of labor required: {wallSpace / 112 * 8}\nThe cost of the paint: {(wallSpace / 112 * 1)*paintPrice}\nThe labor charges: {(wallSpace / 112 * 8)*35}\nThe total cost of the paint job: {(wallSpace / 112 * 1)*paintPrice + (wallSpace / 112 * 8)*35}"
)
