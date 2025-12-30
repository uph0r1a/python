from calendar import monthrange
month, year = tuple(map(int, input().split()))
print(tuple(monthrange(year, month))[1])
