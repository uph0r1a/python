a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for n in a:
    if n < 5:
        b.append(n)
[print(str(n) + " " if n < 5 else "", end="") for n in a]
print()
[print(str(n) + " ", end="") for n in b]
print()
c = int(input("Enter a number: "))
[print(str(n) + " " if n < c else "", end="") for n in a]
