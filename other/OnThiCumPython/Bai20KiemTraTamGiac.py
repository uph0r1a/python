def checkTriangle(a:int , b:int, c:int):
    if c**2 == a**2 + b**2:
        define = "tam giac vuong"
    elif a == b == c:
        define = "tam giac deu"
    elif a == b or b == c or a == c:
        define = "tam giac can"
    elif c**2 < a**2 + b**2:
        define = "tam giac nhon"
    elif c**2 > a**2 + b**2:
        define = "tam giac tu"
    
    if define:
        return f"{a}, {b}, {c} la ba canh cua {define}"
    else:
        return f"{a}, {b}, {c} không la ba canh của mot tam giac"
        

with open("test.inp", "r") as f:
    a, b ,c = map(float, sorted(f.readlines()))

result = checkTriangle(a, b , c)

with open("test.out", "w") as f:
    print(result)
    f.write(result)