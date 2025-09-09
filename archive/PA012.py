# Bài 3
n = int(input("n:"))
if len(str(n)) == 1:
    print("Tổng các chữ số của số", n, "bằng", n)
else:
    print("Tổng các chữ số của số", n, "bằng", int(str(n)[0]) + int(str(n)[1]))
