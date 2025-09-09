k = int(input("Nhập số k >"))
primenumbers = []
if k > 1:
    for i in range(2, k + 1):
        flag = True
        for x in range(2, i):
            if i % x == 0:
                flag = False
                break
        if flag:
            primenumbers.append(str(i))
else:
    raise ValueError("Số phải lớn hơn 1")

print(" ".join(primenumbers))
