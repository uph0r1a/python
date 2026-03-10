sum = 0
for i in range(5):
    print(f"Enter the number of bugs collected for day {i + 1}: ", end="")
    sum += int(input())

print(f"Total bugs collected: {sum}")
