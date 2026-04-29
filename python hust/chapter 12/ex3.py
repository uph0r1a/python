def lines(n):
    if n == 0:
        return
    lines(n - 1)
    print(n * "*")


lines(5)
