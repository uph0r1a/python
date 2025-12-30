with open("test.inp", "r") as f:
    n, k = map(int, f.read().split())

def factorial(n: int):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

fac_n = factorial(n)
fac_k = factorial(k)
fac_nk = factorial(n-k)
result = int(fac_n/(fac_k*fac_nk))

with open("test.out", "w") as f:
    f.write(str(result))