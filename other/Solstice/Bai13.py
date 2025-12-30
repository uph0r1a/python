TS, MS = map(int, input().split())

for i in range(min(TS,MS), 1, -1):
    if TS % i == 0 and MS % i == 0:
        common = i
        break

TS = int(TS / common)
MS = int(MS / common)

print(TS, MS)