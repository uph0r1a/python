def isOdd(pockets):
    if pockets % 2 == 0:
        return False
    return True


print("Enter pockets number: ", end="")
pockets = int(input())

if pockets == 0:
    print("Green")
elif 1 <= pockets <= 10:
    if isOdd(pockets):
        print("Red")
    else:
        print("Black")
elif 11 <= pockets <= 18:
    if isOdd(pockets):
        print("Black")
    else:
        print("Red")
elif 19 <= pockets <= 28:
    if isOdd(pockets):
        print("Red")
    else:
        print("Black")
elif 29 <= pockets <= 36:
    if isOdd(pockets):
        print("Black")
    else:
        print("Red")
else:
    print("Invalid number")
