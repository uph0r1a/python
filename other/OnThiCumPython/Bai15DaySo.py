with open("test.inp", "r") as f:
    _, numbers = f.readlines()
    numbers = list(map(int, numbers.split()))

result = max(numbers) + min(numbers)

with open("test.out", "w") as f:
    f.write(str(result))