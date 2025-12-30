with open("test.inp", "r") as f:
    numbers = list(map(int, f.read().split()))

for i in numbers:
    if i == numbers[-1]:
        break
    currentIndex = numbers.index(i)
    lowestNumber = min(numbers[currentIndex+1:])
    lowestNumberIndex = numbers.index(lowestNumber)
    if i > lowestNumber:
        numbers[currentIndex], numbers[lowestNumberIndex] = numbers[lowestNumberIndex], numbers[currentIndex]

with open("test.out", "w") as f:
    for i in numbers:
        f.write(f"{i} ")