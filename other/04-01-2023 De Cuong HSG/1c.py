n = int(input())
S = 1
flag = True

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)

for i in range(3,n+1,2):
    if flag:
        S += i/factorial(i)
        flag = False
    else:
        S -= i/factorial(i)
        flag = True

print(S)