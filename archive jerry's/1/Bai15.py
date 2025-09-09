a = input("Nhập kí tự >")
if a.isalpha():
    if len(a) == 1:
        print("YES")
    else:
        raise ValueError("Phải là 1 kí tự.")
else:
    print("NO")
