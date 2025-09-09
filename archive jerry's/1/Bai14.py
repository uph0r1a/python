month, year = map(int, input("Nhập tháng và năm >").split())
months31 = (1, 3, 5, 7, 8, 10, 12)
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    if month in months31:
        print("31")
    elif month == 2:
        print("29")
    else:
        print("30")
else:
    if month in months31:
        print("31")
    elif month == 2:
        print("28")
    else:
        print("30")
