with open("test.inp", "r") as f:
    TS, MS = map(int, f.readline().split())

for i in range(min(TS,MS), 1, -1):
    if TS % i == 0 and MS % i == 0:
        TS = int(TS / i)
        MS = int(MS / i)
        break

with open("test.out", "w") as f:
    f.write(f"{TS} {MS}")