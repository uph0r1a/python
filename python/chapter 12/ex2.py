def multiplication(x, y):
    if y == 0:
        return 0
    else:
        return x + multiplication(x, y - 1)


print(multiplication(2, 5))
