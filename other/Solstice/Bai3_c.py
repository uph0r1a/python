N, M = map(int, input().split())

NChiaHet = []
MChiaHet = []
for i in range(1,N+1):
    if N % i == 0:
        NChiaHet.append(i)
for i in range(1,M+1):
    if M % i == 0:
        MChiaHet.append(i)

common1 = set(NChiaHet).intersection(set(MChiaHet))

BoiCuaM = []
BoiCuaN = []
hello = 1
while True:
    BoiCuaM.append(M*hello)
    BoiCuaN.append(N*hello)
    common2 = set(BoiCuaM).intersection(set(BoiCuaN))
    if common2:
        break
    hello += 1
print(max(common1))
print(min(common2))