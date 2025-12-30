TS, MS = map(int, input().split())

if TS % MS == 0:
    print(int(TS/MS))

else:
    for i in range(min(TS,MS), 1, -1):
        if TS % i == 0 and MS % i == 0:
            common = i
            break


    TS = int(TS / common)
    MS = int(MS / common)


    HonSo = TS//MS
    if HonSo == 0:
        print(TS,MS)
    else:
        TS = TS % MS
        print(HonSo, TS, MS)