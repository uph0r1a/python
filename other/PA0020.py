# Bài 1
A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))
delta = B * B - 4 * A * C
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("Phương trình có nghiệm kép ")
    print("x = ", -B/(2 * A))
else:
    print("Phương trình có hai nghiệm phân biệt ")
print("x1=",(- B + delta ** (1 / 2))/ (2 * A))
print("x2=",(- B - delta **(1/2)) / (2 * A))
# Giải thích kết quả
# Đầu tiên ta nhập 3 số thực A,B,C vào phần terminal của chương trình sau đó máy tính sẽ xét điều kiện delta phù hợp với điều kiện nào thì máy tính sẽ tiếp tục với câu lệnh đấy và câu lệnh khác bị bỏ từ đó sẽ ra nghiệm của chương trình