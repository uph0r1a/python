n = input("Nhập n >")
if float(n) > 10**18:
    raise ValueError("Phải nhỏ hơn 10^18")
try:
    number = 0
    sum = 0
    k, a = n.split(".")
    for i in a:
        sum += int(i)
        number += 1

except Exception:
    pass
print(f"Số chữ số thập phân là {number}")
print(f"Tổng của các chữ số thập phân là {sum}")
