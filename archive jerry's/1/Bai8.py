try:
    a, b, c, d = map(int, input(">").split())
except ValueError:
    print("Cần chính xác 4 Số")

if a > b or c > d:
    raise ValueError("Số Không Hợp Lệ.")

if a <= c <= b:
    print("Có điểm chung")
elif a <= d <= b:
    print("Có điểm chung")
else:
    print("Không có điểm chung")
