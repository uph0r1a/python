with open("test.inp", "r") as f:
    TuSo, MauSo = map(int, f.read().split())
if TuSo % MauSo == 0:
    with open("test.out", "w") as f:
        result = TuSo / MauSo
        f.write(f"{int(result)}")
else:
    for i in range(min(TuSo, MauSo), 0, -1):
        if TuSo % i == 0 and MauSo % i == 0:
            TuSo = int(TuSo / i)
            MauSo = int(MauSo / i)
            break

    HonSo = TuSo // MauSo
    
    with open("test.out", "w") as f:
        if HonSo != 0:
            TuSo -= HonSo*MauSo
            f.write(f"{HonSo} {TuSo} {MauSo}")
        else:
            f.write(f"{TuSo} {MauSo}")