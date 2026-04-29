numbers = []

for i in range(20):
    value = float(input(f"Enter number {i + 1}: "))
    numbers.append(value)

lowest = min(numbers)
highest = max(numbers)
total = sum(numbers)
average = total / len(numbers)

print(
    f"\nLowest number: {lowest}\n"
    f"Highest number: {highest}\n"
    f"Total of numbers: {total}\n"
    f"Average of numbers: {average}"
)
