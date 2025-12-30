KW = int(input(">"))
if KW < 0:
    raise ValueError("Số không hợp lệ")
elif 1 <= KW <= 50:
    print(KW*1678)
elif 51 <= KW <= 100:
    print(KW*1734)
elif 101 <= KW <= 200:
    print(KW*2014)
elif 201 <= KW <= 300:
    print(KW*2536)
elif 301 <= KW <= 400:
    print(KW*2834)
else:
    print(KW*2927)
