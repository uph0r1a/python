p, q, r = tuple(map(int, input().split()))
if q // p:
    commonratio = q // p
    if q * commonratio == r:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
