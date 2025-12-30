n = int(input())
flag = False
for i in range(2,n):
    if n % i == 0:
        flag = True
        break

if flag:
    print(f"{n} không là số nguyên tố")
else:
    print(f"{n} là số nguyên tố")