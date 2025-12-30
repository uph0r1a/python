# Bài 3
import math
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if not ((a > 0) and (b > 0 ) and (c > 0) and (a + b > c)and (a + c > b) and (b + c > a)):
    print('Không là 3 cạnh của 1 tam giác ')
elif c == math.sqrt( a * a + b * b) :
    print('Là 3 cạnh của tam giác vuông')
else:
    print('Là 3 cạnh của tam giác')