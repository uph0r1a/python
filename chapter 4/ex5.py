print("Enter the number of year: ", end="")
numberOfyear = int(input())
sum = 0

for i in range(1, numberOfyear + 1):
    for j in range(1, 13):
        print(f"Enter the rainfall in month {j}: ", end="")
        sum += float(input())

print(
    f"Number of month: {numberOfyear * 12}\nTotal inches of rainfall: {sum}\nAverage rainfall per month: {sum / (numberOfyear * 12)}"
)
