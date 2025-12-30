n = int(input())
HelloXD = []
for i in range(1,n):
    if n % i == 0:
        HelloXD.append(i)

if sum(HelloXD) == n:
    print(f"{n} là số hoàn hảo!")
else:
    print(f"{n} không phải là số hoàn hảo")