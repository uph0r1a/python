m, n, k = map(int, input("Nhập m, n, k >").split())
if m * n * k // 10 > 0:
    if m * n * k % 10 == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
