def main():
    day, month, year = map(int,retrieve_info())
    leap: bool = leapYear(year)
    result = add1Day(day, month, year, leap)
    yeuEilam(result)


def retrieve_info():
    with open("test.inp", "r") as f:
        return f.read().split()


def leapYear(year: int):
    if year % 4 == 0:
        return True
    elif year % 4  == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    return False


def add1Day(day: int, month: int, year: int, leap: bool):
    Month31Day = [1,3,5,7,8,10,12]
    Month30Day = [4,6,9,11]
    day += 1

    if month in Month30Day and day == 31:
        month += 1
        day = 1
    elif month in Month31Day and day == 32:
        month += 1
        day = 1
    else: # February
        if leap and day == 30:
            month += 1
            day = 1
        else:
            if day == 29:
                month += 1
                day = 1
    
    if month == 13:
        month = 1
        year += 1

    return f"{day} {month} {year}"


def yeuEilam(Solstice: str):
    with open("test.out", "w") as f:
        f.write(Solstice)




if __name__ == "__main__":
    main()