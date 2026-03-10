sum = i = 0

while i >= 0:
    print("Enter positive number: ", end="")
    i = int(input())
    if i >= 0:
        sum += i

print(f"Sum: {sum}")
