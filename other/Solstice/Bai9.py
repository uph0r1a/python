a, b , c = map(int, input().split())
if (a+b) % c == 0:
    print(0)
else:
    remainder = (a+b) % c
    print(c-remainder)
