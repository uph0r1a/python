with open("test.inp", "r") as f:
    Alpha, Beta = f.readlines()
    Beta = Beta.replace(" ", "").lower()
    Alpha = Alpha[:-1].lower()


count = 0
flag = False
while True:

    if flag:
        break

    for char in Beta:
        index = Alpha.find(char)

        if index == -1:
            flag = True
            break
        elif char == Beta[-1]:
            count += 1
            Alpha = Alpha.replace(Alpha[index], "", 1)
        else:
            Alpha = Alpha.replace(Alpha[index], "", 1)
            
with open("test.out", "w") as f:
    f.write(str(count))