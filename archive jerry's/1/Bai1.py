for i in range(200, 3201):
    if i % 7 == 0 and not i % 5 == 0:
        print(i, end=",")
