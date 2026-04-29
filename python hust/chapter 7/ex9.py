population = []

try:
    with open("files/USPopulation.txt") as file:
        for line in file:
            population.append(int(line.strip()))

except Exception as e:
    print(f"\nError: {e}")

changes = []

for i in range(1, len(population)):
    changes.append(population[i] - population[i - 1])

average_change = sum(changes) / len(changes)

greatest_increase = max(changes)
smallest_increase = min(changes)

greatest_year = 1950 + changes.index(greatest_increase) + 1
smallest_year = 1950 + changes.index(smallest_increase) + 1

print(
    f"\nAverage annual population change: {average_change}\n"
    f"Greatest population increase: {greatest_increase} in {greatest_year}\n"
    f"Smallest population increase: {smallest_increase} in {smallest_year}"
)
