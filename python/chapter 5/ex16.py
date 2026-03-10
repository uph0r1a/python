import random


def isEven(number):
    if number % 2 == 0:
        return True
    return False


countEven = countOdd = 0

for i in range(0, 100):
    number = random.getrandbits(32)
    if isEven(number):
        countEven += 1
    else:
        countOdd += 1

print(f"{countEven} even number\n{countOdd} odd number")
