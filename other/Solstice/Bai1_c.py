def factorial(number: int):
    result = 1
    for i in range(2, number+1):
        result *= i
    return result
n = int(input())
S = 0
for i in range(1,n+1):
    S += (i/factorial(i))
print(S)