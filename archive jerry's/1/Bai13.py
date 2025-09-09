year = int(input("Nhập năm >"))
if year % 400 == 0:
    print("366")
elif year % 4 == 0:
    if year % 100 != 0:
        print("366")
else:
    print("365")
