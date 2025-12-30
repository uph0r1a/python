with open("test.inp") as f:
    value = int(f.read())

result = 0
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(1, value+1):
    result += i

result = result % 26

with open("test.out", "w") as f:
    f.write(characters[result])
