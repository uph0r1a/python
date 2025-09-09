primenumbers = [2, 3, 5, 7]

a, b = map(int, input("Nhập a và b >").split())
if a <= 1 or b <= 1:
    raise ValueError("a và b phải lớn hơn 1")

ab = [a, b]
primea = []
primeb = []
gen = [primea, primeb]

for i in range(0, 2):
    n = ab[i]
    alist = gen[i]
    while n != 1:
        for i in primenumbers:
            if n % i == 0:
                n /= i
                alist.append(i)

common = [x for x in primea if x in primeb]
if common:
    # Ước Chung Nhỏ Nhất
    UCNN = 1
    for i in common:
        UCNN *= i
    print(UCNN)

    # BCNN
    for i in common:
        primea.remove(i)
        primeb.remove(i)

    BCNN = 1
    for i in common:
        BCNN *= i
    for i in primea:
        BCNN *= i
    for i in primeb:
        BCNN *= i
    print(BCNN)

else:
    print("Không có bội chung hay ước chung")
