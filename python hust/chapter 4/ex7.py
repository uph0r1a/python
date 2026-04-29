print("Enter the number of days: ", end="")
numberOfDays = int(input())
salary = 1
sum = 0

print(f"{"Day":<10}{"Salary":<10}\n----------------")

for i in range(1, numberOfDays + 1):
    print(f"{i:<10}{salary}")
    sum += salary
    salary *= 2

print(f"----------------\nTotal pay: {sum}")
