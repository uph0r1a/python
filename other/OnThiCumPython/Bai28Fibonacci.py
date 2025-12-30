with open("test.inp", "r") as f:
    value = int(f.read())



current = 1
before = 0
aCopy = current
for i in range(2, value + 1):
        aCopy = current
        current += before
        before = aCopy

with open("test.out", "w") as f:
    if value == 0:
        f.write("0")
    else:
        f.write(str(current))
