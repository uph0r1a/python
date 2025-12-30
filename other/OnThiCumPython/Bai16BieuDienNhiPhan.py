from itertools import permutations
with open("test.inp", "r") as f:
    number = int(f.read())
binary = str(bin(number))[2:]

highest = 0
combinations = [''.join(i) for i in permutations(binary, len(binary))]
for sex in combinations:
    realSex = int(sex, 2)
    if realSex > highest:
        highest = realSex

with open("test.out", "w") as f:
    f.writelines(f"{binary}\n{highest}")       