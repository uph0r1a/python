string = input("Enter a string: ")
result = ""

for i, c in enumerate(string):
    if c.isupper() and i != 0:
        result += " " + c
    else:
        result += c

print(result)
