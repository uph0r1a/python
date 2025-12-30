with open("test.inp", "r") as f:
    string = f.readline()
highest = 0
current = 1
index = 1
for i in string[1:]:
    if i == string[index - 1]:
        current += 1
    else:
        if current > highest:
            highest = current
        current = 1
    index += 1

# Just for good measure
if current > highest:
    highest = current
with open("test.out", "w") as f:
    f.write(str(highest))