a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if not ((a > 0) and (b > 0) and (c > 0) and (a + b > c) and (a + c > b) and (b + c > a)):
    print("Không phải là cạnh của tam giác")
elif (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (c**2 + b**2 == a**2):
    print("Là ba cạnh tam giác vuông")
else:
    print("Là ba cạnh của tam giác")
