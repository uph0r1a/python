myreaction = []
for i in range(1, 101):
    myreaction.append(i)
myreaction.reverse()
for i in range(1, 11):
    for i2 in range(1, 11):
        print(myreaction[0], end="  ")
        del myreaction[0]
    if i != 10:
        print()
