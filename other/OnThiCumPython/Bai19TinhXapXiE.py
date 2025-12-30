def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

with open("test.inp", "r") as f:
    limit = int(f.read()) + 1

result = 2.0

for i in range(2,limit):
    result += 1/factorial(i)

with open("test.out", "w") as f:
    f.write(str(result))