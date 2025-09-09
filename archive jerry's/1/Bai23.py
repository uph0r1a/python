from math import sqrt as w

n = int(input("Nhập số nguyên dương n >"))
if 0 < n <= 100:
    print("fn =", int((1 / w(5) * (((1 + w(5)) / 2) ** n - ((1 - w(5)) / 2) ** n))))
else:
    raise ValueError("Số phải lớn hơn 0 và nhỏ hơn hoặc bằng 100")
