with open("test.inp", "r") as f:
    number = f.read()
sum = 0
for i in number:
    sum += int(i)

with open("test.out", "w") as f:
    f.writelines(f"{len(number)}\n{sum}")