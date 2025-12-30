with open("test.inp", "r") as f:
    a, b , c = map(int, f.read().split())
result = c - (a+b) % c
with open("test.out", "w") as f:
    f.write(str(result))