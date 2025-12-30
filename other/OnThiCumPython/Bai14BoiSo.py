with open("test.inp", "r") as f:
    k , m ,n = map(int, f.read().split())
counter = 0
for i in range(1, n + 1):
    if i % k == 0 or i % m == 0:
        counter += 1

with open("test.out", "w") as f:
    f.write(str(counter))