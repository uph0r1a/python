N = int(input("Nhap N: "))
M = int(input("Nhap M: "))

for i in range(min(N, M), 1 , -1):
    if N % i == 0 and M % i == 0:
        common = i
        break

# BoiCuaM = set()
# BoiCuaN = set()
# index = 1
# while True:
#     BoiCuaM.add(N*index)
#     BoiCuaN.add(M*index)

#     common2 = BoiCuaM.intersection(BoiCuaN)

#     if common2:
#         break
#     index += 1

tich = M * N
common2 = tich / common


print(common) # UCNN
print(int(common2)) # BCLN




