while True:
    a = int(input("Nhập A >"))
    b = int(input("Nhập b >"))
    if a != 0 and b != 0:
        break
    else:
        print("Cả 2 số phải khác 0.")
print("x =", (-b / a))
