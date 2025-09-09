# Bài 6
import math

a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(s)
