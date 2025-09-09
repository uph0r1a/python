n = int(input())
if n < 0 or 99 < n:
    raise ValueError("Phải là số không âm dưới 99.")
a = n // 10
b = n % 10
print("Tổng các chữ số của số", n, "bằng", a + b)
