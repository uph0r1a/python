a = input()
if "." in a:
    number, decimal = a.split(".")
    firstDecimal = int(decimal[0])

    if firstDecimal >= 5:
        a = int(float(a)) + 1
    elif firstDecimal == 4:
        lastNum: int = firstDecimal
        for i in decimal[1:]:
            if int(i) >= 5 and lastNum >= 4:
                a = int(float(a)) + 1
                break
            elif int(i) == 4:
                lastNum = int(i)
                continue
            else:
                break
    else:
        a = int(float(a))
print(a)
