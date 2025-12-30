with open("test.inp", "r") as f:
    value = int(f.read())

start = int("1" + "0"*(value - 1))
end = int("9"*value)
counter = 0
for i in range(start, end + 1):
    if str(i) == str(i)[::-1]:
        counter += 1

with open("test.out", "w") as f:
    f.write(str(counter))