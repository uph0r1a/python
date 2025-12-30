with open("test.inp", "r") as f:
    sex: list = f.readlines()
    checkPoints: list= []

    for i in sex:
        checkPoints.append(tuple(i.split()))

currentPassengers: int = int(checkPoints[0][1])
highest: int = int(currentPassengers)


for i in checkPoints[1:]:
    currentPassengers += int(i[1])
    currentPassengers -= int(i[0])
    if currentPassengers > highest:
        highest = currentPassengers

with open("test.out", "w") as f:
    f.write(str(highest))