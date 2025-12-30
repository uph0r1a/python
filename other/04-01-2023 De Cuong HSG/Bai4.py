K = int(input("Nhap K: "))
M = int(input("Nhap M: "))
N = int(input("Nhap N: "))
count = 0
for i in range(1, N+1):
    if i % N == 0 and i % M == 0:
        count += 1

print(count)