n = int(input())
results = []
for i in range(2,n+1):
    flag = False
    for number in range(2,i):
        if i % number == 0:
            flag = True
            break
    
    if flag:
        pass
    else:
        results.append(i)

for result in results:
    print(result, end=" ")