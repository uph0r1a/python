telNumber = input("Enter a 10-character telephone number: ")
result = ""

for c in telNumber.upper():
    if c in ("A", "B", "C"):
        result += "2"
    elif c in ("D", "E", "F"):
        result += "3"
    elif c in ("G", "H", "I"):
        result += "4"
    elif c in ("J", "K", "L"):
        result += "5"
    elif c in ("M", "N", "O"):
        result += "6"
    elif c in ("P", "Q", "R", "S"):
        result += "7"
    elif c in ("T", "U", "V"):
        result += "8"
    elif c in ("W", "X", "Y", "Z"):
        result += "9"
    else:
        result += c

print(result)
