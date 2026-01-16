name = input("Enter a name: ")
innitials = ""

for i in range(len(name)):
    if i == 0:
        innitials += name[i]

    if name[i] == " ":
        innitials += "." + name[i + 1]

print(innitials)
