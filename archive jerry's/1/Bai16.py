atuple = tuple(map(int, input("Nhập 3 độ dài a, b, c >").split()))
a, b, c = sorted(atuple)
if abs(a - b) < c < a + b:
    if a**2 + b**2 == c**2:
        print("Vuông")
    elif a == b == c:
        print("Đều")
    elif a == b or a == c:
        print("Cân")
    else:
        print("Thường")
else:
    raise ValueError("Không phải là tam giác")
