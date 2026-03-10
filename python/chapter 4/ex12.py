print("Enter a nonnegative interger: ", end="")
number = int(input())
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f"{number}! = {factorial}")
