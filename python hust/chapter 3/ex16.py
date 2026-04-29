print("Enter year: ", end="")
year = int(input())

if (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(f"In {year} February has 29 days")
else:
    print(f"In {year} February has 28 days")
