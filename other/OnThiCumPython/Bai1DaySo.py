with open("test.inp", "r") as f:
    lol = []
    for i in f.readlines():
        lol.append(i)
    lol = list(map(int, lol[1].split()))
highest = 0
highestNumber = 0
for i in lol:
    sum = 0
    for number in str(i):
        sum += int(number)
    
    if sum > highest:
        highest = sum
        highestNumber = i

with open("test.out", "w") as f:
    f.write(str(highestNumber))