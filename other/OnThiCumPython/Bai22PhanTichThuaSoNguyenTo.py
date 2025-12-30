with open("test.inp", "r") as f:
    value = int(f.read())

list = []
while value != 1:
    for i in range(value, 1, -1):
        if value % i == 0:
            flag = True
            for x in range(2, i):
                if i % x == 0:
                    flag = False
                    break
            
            if flag:
                value /= i
                value = int(value)
                list.append(i)

filtered = sorted(set(list))

thisIsSoInefficient = False
result = ""
for i in filtered:
    if thisIsSoInefficient:
        count = list.count(i)
        result = result + f"\n{i} {count}"
    else:
        count = list.count(i)
        result = result + f"{i} {count}"
        thisIsSoInefficient = True


with open("test.out", "w") as f:
    f.write(result)