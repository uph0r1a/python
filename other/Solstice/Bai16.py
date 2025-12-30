n = int(input())
k = int(input())
results = []
for i in range(n+1):
    x = i % 10
    if x == k:
        results.append(i)
print(len(results))