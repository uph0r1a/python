# Bài 6
a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))
if abs(a - b) < c < (a + b):
    print("YES")
else:
    print("NO")
