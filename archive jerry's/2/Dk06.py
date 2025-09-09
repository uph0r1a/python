a, b = map(int, input().split())
if a == 0 and b == 0:
    print("INF")
elif a == 0 and b != 0:
    print("NO")
elif a != 0 and b == 0:
    print("0")
else:
    result = -b / a
    print(f"{result:.2f}")
