print("Enter the number of males: ", end="")
males = int(input())

print("Enter the number of females: ", end="")
females = int(input())

print(
    f"Percentage of males: {(males/(males+females)) * 100}%\nPercentage of females: {(females/(males+females)) * 100}%"
)
