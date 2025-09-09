n = int(input("Nhập n >"))
if 2 > n:
    raise ValueError("Số phải lớn hơn 1")


primenumbers = []
result = []


for i in range(2, n + 1):
    flag = True
    for x in range(2, i):
        if i % x == 0:
            flag = False
            break
    if flag:
        primenumbers.append(i)

primenumbers.reverse()

while n > 1:
    for i in primenumbers:
        if n % i == 0:
            n /= i
            result.append(str(i))


result.reverse()


print(" ".join(result))
