with open("test.inp", "r") as f:
    information = int(f.readline())

for i in range(information, 0, -1):
    if str(i) == str(i)[::-1]:
        information = str(i)
        break

with open("test.out", "w") as f:
    f.write(information)
