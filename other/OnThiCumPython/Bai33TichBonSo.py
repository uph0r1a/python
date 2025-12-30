with open("test.inp", "r") as f:
    numbers = list(map(float, f.readlines()))
result = 1
for i in numbers:
    result *= i
if result > 0 :
    result = "1"
elif result < 0:
    result = "-1"
else:
    result = "0"

with open("test.out", "w") as f:
    f.write(result)
    