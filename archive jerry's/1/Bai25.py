n = int(input("Cho số n >"))

if n < 0 or n > 15:
    raise ValueError("Số phải lớn hơn 0 và nhỏ hơn 15")
elif n == 0:
    print(1)
    quit()

for i in range(1, n):
    n *= i

print(n)
