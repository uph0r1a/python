# Bài 4
n = int(input("n:"))
if len(str(n)) == 1:
    print("Tổng các chữ số của số", n, "bằng", n)
elif len(str(n)) == 3:
    print(
        "Tổng các chữ số của số",
        n,
        "bằng",
        int(str(n)[0]) + int(str(n)[1]) + int(str(n)[2]),
    )
else:
    print("Tổng các chữ số của số", n, "bằng", int(str(n)[0]) + int(str(n)[1]))
