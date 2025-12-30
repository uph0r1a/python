k = int(input())
m = int(input())
n = int(input()) # Pham Vi
result = 0
for i in range(1,n+1):
    if i % k == 0 or i % m == 0:
        result += 1

print(result)