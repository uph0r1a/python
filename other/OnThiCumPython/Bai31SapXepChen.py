with open("test.inp", "r") as f:
    numbers = list(map(int, f.read().split()))


for i in numbers:
    currentIIndex = numbers.index(i)
    for x in numbers[:currentIIndex]:
        if x > i:
            currentXIndex = numbers.index(x)
            numbers.pop(currentIIndex)
            numbers[currentXIndex:currentXIndex] = [i]
            break

with open("test.out", "w") as f:
    result = ""
    for i in numbers:
        result = result + str(i) + " "
    f.write(result)