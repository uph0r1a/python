while True:
    a = float(input("Nhập a >"))
    b = float(input("Nhập b >"))
    if a != 0 and a != -b:
        break
    else:
        print("Không thỏa mãn điều kiện.")
print("x =", (-b / a))
