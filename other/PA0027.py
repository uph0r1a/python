# Bài 1
from sys import exit as byebye
try:
    a, b, c, d = map(int, input(">").split())
except ValueError:
    print("Quá Nhiều Số. (Cần 4)")

if a > b or c > d:
    raise ValueError("Số Không Hợp Lệ.")

for i in range(a, b + 1):
    if i in range(c, d+1):
        print("Có điểm chung")
        byebye()
print("Không có điểm chung")