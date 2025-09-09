n = int(input("Nhập số n >"))
if n < 2:
    print("NO")
    quit()

flag = True
for i in range(2, n):
    if n % i == 0:
        flag = False
        break
if flag:
    print("YES")
else:
    print("NO")
