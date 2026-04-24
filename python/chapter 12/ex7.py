def power(n, exp):
    if exp == 0:
        return 1
    return n * power(n, exp - 1)


print(power(3, 3))
