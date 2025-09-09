a, b = map(int, input("Nhập a và b >").split())
if a <= 1 or b <= 1:
    raise ValueError("a và b phải lớn hơn 1")


ab = [a, b]


primea = []
primeb = []
primecon = [primea, primeb]


timesa = []
timesb = []
timescon = [timesa, timesb]

divivea = []
diviveb = []
diviable = [divivea, diviveb]

# a/b chứa những số nguyên tố nào
for p in range(0, 2):
    n = ab[p]
    primex = primecon[p]
    for i2 in range(2, n + 1):
        flag = True
        for i3 in range(2, i2):
            if i2 % i3 == 0:
                flag = False
                break
        if flag:
            primex.append(i2)

# Ko cần 2 dòng này lắm xd xd xd xd
primea.reverse()
primeb.reverse()


# a/b là tích của những số nguyên tố nào
for i in range(0, 2):
    n = ab[i]
    times = timescon[i]
    prime = primecon[i]
    divide = diviable[i]

    # Số nguyên tố nào chia được
    for number in prime:
        if n % number == 0:
            divide.append(number)

    # Tìm các số nguyên tố tạo nên tích a/b
    while n != 1:
        for i2 in divide:
            if n % i2 == 0:
                n /= i2
                times.append(i2)


# Nguyên tố Chung
common = []
for z in timesa:
    if z in timesb:
        common.append(z)
        timesa.remove(z)
        timesb.remove(z)

if common:
    # Ước Chung Nhỏ Nhất
    UCNN = 1
    for h in common:
        UCNN *= h
    print(UCNN)

    # Bội Chung Nhỏ Nhất
    BCNN = 1
    for v in common:
        BCNN *= v
    for d in timesa:
        BCNN *= d
    for r in timesb:
        BCNN *= r
    print(BCNN)
else:
    print("Không có bội chung hay ước chung.")
