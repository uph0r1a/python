with open("test.inp", "r") as f:
    start, end = map(int, f.read().split())

counter = 0
for i in range(start, end + 1):
    if str(i) == str(i)[::-1]:
        counter += 1

with open("test.out", "w") as f:
    f.write(str(counter))