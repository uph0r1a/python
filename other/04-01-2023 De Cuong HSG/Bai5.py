Day31Months = [1,3,5,7,8,10,12]
Day30Months = [4,6,9,11]
month, year = map(int, input().split())
if month in Day30Months:
    print(30)
elif month in Day31Months:
    print(31)
else:
    if year % 4 == 0 and year % 100 != 0:
        print(29)
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        print(29)
    else:
        print(28)